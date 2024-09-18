"""
TASK 1
create a command line or GUI  based application using python, allowing users to create , update , 
and track their To-Do Lists.
"""
import os

# Initialize an empty to-do list
todo_list = []
print("welcome to your do to list:)")
print("---------------------------")
# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1 To View To-Do List")
    print("2 To Add a Task")
    print("3 To Update a Task")
    print("4 To Delete a Task")
    print("5 To Mark Task as Done")
    print("6 To Exit")

# Function to view the to-do list
def view_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['task']} [{status}]")

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully.")

# Function to update an existing task
def update_task():
    view_list()
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(todo_list):
        new_task = input("Enter the updated task: ")
        todo_list[task_number]['task'] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid task number, please enter valid task number")

# Function to delete a task
def delete_task():
    view_list()
    task_number = int(input("Enter the task number that is to be deleted : ")) - 1
    if 0 <= task_number < len(todo_list):
        del todo_list[task_number]
        print("Task deleted successfully.")
    else:
        print("Invalid task number,please enter valid task number")

# Function to mark a task as done
def mark_done():
    view_list()
    task_number = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]['done'] = True
        print("Task marked as done.")
    else:
        print("Invalid task number,please enter valid task number")

# Main loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_done()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()