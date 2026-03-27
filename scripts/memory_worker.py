#!/usr/bin/env python3
import json
import os
import time
import uuid
from pathlib import Path
import sys
import fcntl

WORKSPACE_PATH = Path('/root/.openclaw/workspace')
QUEUE_DIR = WORKSPACE_PATH / 'runtime' / 'async_queue'
TASKS_DIR = QUEUE_DIR / 'tasks'
TASKS_FILE = QUEUE_DIR / 'tasks.jsonl'
LOCK_FILE = QUEUE_DIR / 'queue.lock'
STALE_LOCK_SECONDS = 300  # 5 minutes

def acquire_lock():
    """Acquires a lock, returning the lock file handle or None."""
    lock_fp = open(LOCK_FILE, 'w')
    try:
        fcntl.flock(lock_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        # Check for stale lock by reading its content
        lock_fp.seek(0)
        content = lock_fp.read().strip()
        if content:
            try:
                pid, timestamp = content.split(':')
                if time.time() - float(timestamp) <= STALE_LOCK_SECONDS:
                    # Still a valid lock held by another process
                    fcntl.flock(lock_fp, fcntl.LOCK_UN)
                    lock_fp.close()
                    return None
                else:
                    print(f"Found stale lock from PID {pid}. Overriding.", file=sys.stderr)
            except (ValueError, IndexError):
                # Malformed lock content — treat as stale
                print("Malformed lock content. Treating as stale.", file=sys.stderr)
        
        # Write new lock info
        lock_fp.seek(0)
        lock_fp.truncate()
        lock_fp.write(f"{os.getpid()}:{time.time()}")
        lock_fp.flush()
        return lock_fp
    except (IOError, BlockingIOError):
        lock_fp.close()
        return None

def release_lock(lock_fp):
    """Releases the lock and removes the lock file."""
    if lock_fp:
        fcntl.flock(lock_fp, fcntl.LOCK_UN)
        lock_fp.close()
        # No need to remove file, flock is enough. It will be overwritten next time.

def find_task():
    """Finds the first 'queued' task in the tasks file."""
    if not TASKS_FILE.exists():
        return None, []
    
    with open(TASKS_FILE, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        try:
            task = json.loads(line)
            if task.get('status') == 'queued':
                remaining_lines = lines[:i] + lines[i+1:]
                return task, remaining_lines
        except json.JSONDecodeError:
            continue
    return None, lines

def run_memory_audit():
    """Performs a simple memory audit."""
    report = {
        'key_files_checked': [],
        'memory_dir_file_count': 0,
        'errors': []
    }
    key_files = ['SOUL.md', 'USER.md', 'MEMORY.md', 'AGENTS.md']
    
    for kf in key_files:
        path = WORKSPACE_PATH / kf
        report['key_files_checked'].append({
            'file': kf,
            'exists': path.exists(),
            'size_bytes': path.stat().st_size if path.exists() else 0
        })
        
    try:
        memory_dir = WORKSPACE_PATH / 'memory'
        if memory_dir.is_dir():
            report['memory_dir_file_count'] = len(list(memory_dir.iterdir()))
    except Exception as e:
        report['errors'].append(f"Could not audit memory/ directory: {str(e)}")
        
    return report

def main():
    lock_fp = acquire_lock()
    if not lock_fp:
        print("Worker already running or lock is fresh. Exiting.", file=sys.stderr)
        return

    try:
        task, remaining_lines = find_task()
        if not task:
            print("No queued tasks found.", file=sys.stderr)
            return

        task_id = task.get('task_id')
        report_file = TASKS_DIR / f"{task_id}.json"

        # Update status to running
        task['status'] = 'running'
        task['started_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        with open(report_file, 'w') as f:
            json.dump(task, f, indent=2)

        # Update the main task queue file
        with open(TASKS_FILE, 'w') as f:
            f.writelines(remaining_lines)

        print(f"Processing task {task_id}...")
        
        # --- Perform the actual task ---
        audit_report = run_memory_audit()
        # -----------------------------
        
        # Update status to completed
        task['status'] = 'completed'
        task['completed_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        task['report'] = audit_report
        with open(report_file, 'w') as f:
            json.dump(task, f, indent=2)
            
        print(f"Task {task_id} completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        if 'task' in locals() and task:
            task['status'] = 'failed'
            task['error'] = str(e)
            report_file = TASKS_DIR / f"{task.get('task_id')}.json"
            with open(report_file, 'w') as f:
                json.dump(task, f, indent=2)
    finally:
        release_lock(lock_fp)

if __name__ == "__main__":
    main()
