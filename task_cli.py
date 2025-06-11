import sys
import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def generate_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def now():
    return datetime.now().isoformat()

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': generate_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': now(),
        'updatedAt': now()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task["id"]})')

def mark_status(task_id, new_status):
    tasks=load_tasks()
    found=False

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = now()
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task {task_id} marked as {new_status}.")
    else:
        print("Task not found.")

# Command handler
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "mark-in-progress" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_status(task_id, "in-progress")
        except ValueError:
            print("Task ID must be an integer.")

    elif command == "mark-done" and len(sys.argv) == 3:
        try:
            task_id = int(sys.argv[2])
            mark_status(task_id, "done")
        except ValueError:
            print("Task ID must be an integer.")
    else:
        print("Invalid command or missing arguments")

if __name__ == "__main__":
    main()
    print("Done")