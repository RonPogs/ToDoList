# todo_list.py

# Task List - In a real-world app, this would probably be stored in a file or database
tasks = []

# Task structure could be a dictionary, or a custom class if you need more features.
class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

# Function to display all tasks
def view_all_tasks():
    if not tasks:
        print("No tasks to display.")
    else:       
        print("Current tasks:")
for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")
# Function to add a new task
def add_task():
    task_name = input("Enter the name of the new task: ")
    new_task = Task(task_name)
    tasks.append(new_task)
    print(f"Task '{task_name}' added.")

# Function to filter tasks by completion status
def filter_tasks(status):
    if status == 'completed':
        filtered_tasks = [task for task in tasks if task.completed]
    elif status == 'incomplete':
        filtered_tasks = [task for task in tasks if not task.completed]
    else:
        print("Invalid status. Please use 'completed' or 'incomplete'.")
        return
    print(f"Filtered tasks ({status}):")
    for task in filtered_tasks:
        print(task)

# Function to edit an existing task
def edit_task():
    view_all_tasks()
    try:
        task_index = int(input("Enter the task number to edit: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        new_name = input("Enter the new task name: ")
        tasks[task_index].name = new_name
        print(f"Task updated to '{new_name}'.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to mark a task as completed
def mark_task_complete():
    view_all_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        tasks[task_index].completed = True
        print(f"Task '{tasks[task_index].name}' marked as complete.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")



# Function to delete a task
def delete_task():
    view_all_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task.name}' deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


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
