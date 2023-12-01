import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks registered.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid index!")

# Example of usage:
while True:
    print("\n1. List Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        list_tasks()
    elif choice == '2':
        new_task = input("Enter the new task: ")
        add_task(new_task)
    elif choice == '3':
        list_tasks()
        index_to_remove = int(input("Enter the task number to remove: "))
        remove_task(index_to_remove)
    elif choice == '4':
        break
    else:
        print("Invalid option. Please try again.")
