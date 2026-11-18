from task_manager import (
    load_tasks,
    add_task,
    view_tasks,
    complete_task,
    delete_task,
)


def main():
    """Run the Task Manager command-line application."""
    tasks = load_tasks()

    while True:
        print("\n===== SWYNEX PYTHON TASK MANAGER =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                complete_task(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("Thank you for using the Task Manager!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except (OSError, ValueError) as error:
            print(f"Sorry, the operation could not be completed: {error}")


if __name__ == "__main__":
    main()
