https://roadmap.sh/projects/task-tracker

🛠 Task Tracker CLI

A simple command-line tool written in Python to track your tasks — what needs to be done, what you're currently working on, and what's already done.

This project helps reinforce core programming skills such as:

    Working with the filesystem

    Handling JSON data

    Building command-line interfaces (CLI)

    Managing tasks with basic CRUD operations

✨ Features

    Add new tasks

    Update task descriptions (coming soon)

    Mark tasks as in-progress or done

    View all tasks or filter by status

    Store tasks in a local tasks.json file (auto-created if not present)

📦 Usage

Run from the command line:

# Add a task
python task_cli.py add "Buy groceries"

# Mark a task in progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 1

🔒 Note

This tool is for local personal use. The tasks.json file stores your task list and is not uploaded to GitHub if .gitignore is used.


