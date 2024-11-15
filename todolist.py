# todo_list.py

# Task List - In a real-world app, this would probably be stored in a file or database
tasks = []

# Task structure could be a dictionary, or a custom class if you need more features.
class Task:


# Function to display all tasks
def view_all_tasks():

# Function to add a new task
def add_task():
    task_name = input("Enter the name of the new task: ")
    new_task = Task(task_name)
    tasks.append(new_task)
    print(f"Task '{task_name}' added.")

# Function to filter tasks by completion status
def filter_tasks(status):


# Function to edit an existing task
def edit_task():
    view_all_tasks()


# Function to mark a task as completed
def mark_task_complete():
    view_all_tasks()


# Function to delete a task
def delete_task():
    view_all_tasks()


# Function to quit the program
def exit_program():
    print("Goodbye!")
    exit()

# Main menu to interact with the user
def display_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a Task")
        print("2. View All Tasks")
        print("3. Filter Tasks")
        print("4. Edit a Task")
        print("5. Mark a Task as Complete")
        print("6. Delete a Task")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_all_tasks()
        elif choice == '3':
            status = input("Filter by (completed/incomplete): ").lower()
            filter_tasks(status)
        elif choice == '4':
            edit_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            delete_task()
        elif choice == '7':
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    display_menu()
