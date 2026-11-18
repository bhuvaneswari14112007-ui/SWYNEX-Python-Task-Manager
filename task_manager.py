"""Task management functions and JSON file storage."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load tasks from the JSON file, or return an empty list."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
        if not isinstance(tasks, list):
            raise ValueError("The task data must be a list.")
        return tasks
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Could not read saved tasks ({error}). Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save all tasks to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def next_task_id(tasks):
    """Return an unused task ID."""
    return max((task.get("id", 0) for task in tasks), default=0) + 1


def add_task(tasks):
    """Ask for a task name, validate it, and save it."""
    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty.")
        return

    task = {
        "id": next_task_id(tasks),
        "name": name,
        "completed": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all saved tasks."""
    if not tasks:
        print("No tasks found. Add a task first.")
        return

    print("\n--- YOUR TASKS ---")
    for task in tasks:
        status = "Completed" if task.get("completed") else "Pending"
        print(f'{task["id"]}. {task["name"]} [{status}]')


def get_task_by_id(tasks, prompt):
    """Read and validate a task ID; return the matching task or None."""
    raw_id = input(prompt).strip()
    try:
        task_id = int(raw_id)
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return None

    if task_id <= 0:
        print("Task ID must be a positive number.")
        return None

    for task in tasks:
        if task.get("id") == task_id:
            return task

    print("Task ID not found.")
    return None


def complete_task(tasks):
    """Mark a selected task as completed."""
    task = get_task_by_id(tasks, "Enter the task ID to complete: ")
    if task is None:
        return

    if task.get("completed"):
        print("This task is already completed.")
        return

    task["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")


def delete_task(tasks):
    """Delete a selected task."""
    task = get_task_by_id(tasks, "Enter the task ID to delete: ")
    if task is None:
        return

    tasks.remove(task)
    save_tasks(tasks)
    print("Task deleted successfully.")
