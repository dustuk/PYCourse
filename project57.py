def add_task():
    # get task from user
    task = input("Enter task: ")
    
    # check if task is empty
    if task == "":
        print("Task cannot be empty")
        return
    
    # define task status
    task_info = {
        "task": task,
        "completed": False
    }
    
    # add task to tasks list if not already in the list
    tasks.append(task_info)
    print("Task added to the list successfully")


def mark_task():
    incomplete_tasks = [task for task in tasks if not task["completed"]]
    
    if not incomplete_tasks:
        print("No incomplete tasks")
        return
    
    print("Tasks is incomplete:")
    for i, task in enumerate(incomplete_tasks, 1):
        print(f"{i} - {task['task']}")
        
    task_number = input("choose task to complete (enter to cancel): ")
    
    if task_number == "": return
    
    task_number = int(task_number)
    
    if task_number > len(incomplete_tasks) or task_number < 1: print("Invalid task number"); return

    incomplete_tasks[task_number - 1]["completed"] = True
    print("Task marked completed")
        
           
def view_tasks():
    if not tasks:
        print("No tasks to view")
        return
    
    print(f"Tasks:\n{'-' * 40}")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✕"
        print(f"{i}. {task['task']} {status}")
    print("-" * 40)


massage = """1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit"""

tasks = []

while True:
    print(massage)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # add task to tasks list
        add_task()
    elif choice == "2":
        # mark task as complete
        mark_task()
    elif choice == "3":
        # view tasks
        view_tasks()
    elif choice == "4":
        # quit
        break
    else:
        print("Invalid choice, please enter a number between 1 and 4.")