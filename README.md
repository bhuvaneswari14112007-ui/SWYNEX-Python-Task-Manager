# SWYNEX Python CLI Application — Task Manager

A beginner-friendly command-line task manager built with Python. It allows users to add, view, complete, and delete tasks. Tasks are saved in a JSON file so they remain available after the program closes.

## Features

- Add tasks with input validation
- View all tasks and their status
- Mark tasks as completed
- Delete tasks
- Save tasks in `tasks.json`
- Handle invalid menu choices, invalid task IDs, and file/JSON errors

## Concepts used

- Functions: each operation is implemented in a separate function
- Modules: `main.py` imports functions from `task_manager.py`
- Validation: empty task names and invalid IDs are rejected
- Exception handling: `try/except` handles invalid input and file/JSON errors
- File handling: Python's `json` module stores task data

## Requirements

- Python 3.8 or later
- No third-party packages required

## Run the application

Open a terminal in this project folder and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Menu

1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit

The `tasks.json` file is created automatically when the first task is saved.

## Project structure

```text
SWYNEX-Python-CLI-Application/
├── main.py
├── task_manager.py
└── README.md
```

## GitHub upload

1. Create a new public repository named `SWYNEX-Python-CLI-Application`.
2. Upload `main.py`, `task_manager.py`, and `README.md`.
3. Commit the files.
4. Open the repository and copy its URL for your SWYNEX task submission.

## Author

Add your name here before publishing, if required.
