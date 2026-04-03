# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f" Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_no - 1)
            print(f" Task '{removed}' deleted successfully!")
        except (ValueError, IndexError):
            print(" Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
