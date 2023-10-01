# Updated To-Do List Application in Python

# Create an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task by its index
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Invalid task index.")

# Function to update a task by its index
def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print(f"Task '{new_task}' updated!")
    else:
        print("Invalid task index.")

# Main application loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to remove: "))
        remove_task(index)
    elif choice == "4":
        index = int(input("Enter the task index to update: "))
        new_task = input("Enter the new task: ")
        update_task(index, new_task)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")