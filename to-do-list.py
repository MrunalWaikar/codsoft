import json
import os

# Define the file name where the to-do list will be stored
FILE_NAME = "todo_list.json"

# Load the to-do list from the file if it exists
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        todo_list = json.load(file)
else:
    todo_list = []

def save_todo_list():
    with open(FILE_NAME, "w") as file:
        json.dump(todo_list, file, indent=4)

def display_todo_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, item in enumerate(todo_list, 1):
            status = "Done" if item["done"] else "Not Done"
            print(f"{idx}. {item['task']} [{status}]")
        print()

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    save_todo_list()
    print("Task added successfully.")

def update_task():
    display_todo_list()
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            new_task = input("Enter the new task: ")
            todo_list[task_num - 1]["task"] = new_task
            save_todo_list()
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_as_done():
    display_todo_list()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            save_todo_list()
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_todo_list()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            del todo_list[task_num - 1]
            save_todo_list()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Display to-do list")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_task_as_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
