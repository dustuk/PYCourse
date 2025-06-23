#Task Manager

import datetime

tasks = []

def main(tasks):
    massage = """1 - add tasks to a list
2 - mark task as complete
3 - view tasks
4 - Quit"""

    while True:
        print(massage)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # add task to tasks list
            add_task(tasks)
        elif choice == "2":
            # mark task as complete
            mark_task(tasks)
        elif choice == "3":
            # view tasks
            view_tasks(tasks)
        elif choice == "4":
            # quit
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")
            
            
def add_task(tasks):
    # get task from user
    task = input("Enter task: ")
    
    date = input("Enter task date (yyyy-mm-dd): ")
    
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")    
    except:
        print("Invalid date format, please enter a date in the format yyyy-mm-dd")
        return  
    
    # check if task is empty
    if task == "":
        print("Task cannot be empty")
        return
    
    # define task status
    task_info = {
        "task": task,
        "completed": False,
        "date": date
    }
    
    # add task to tasks list if not already in the list
    tasks.append(task_info)
    print("Task added to the list successfully")


def mark_task(tasks):
    incomplete_tasks = [task for task in tasks if not task["completed"]]
    
    if not incomplete_tasks:
        print("No incomplete tasks")
        return
    
    print("Tasks is incomplete:")
    for i, task in enumerate(incomplete_tasks, 1):
        print(f"{i} - {task['task']}")
     
    try:    
        task_number = input("choose task to complete (enter to cancel): ")
        
        if task_number == "": return
        
        task_number = int(task_number)
        
        if task_number > len(incomplete_tasks) or task_number < 1: 
            print("Invalid task number, please choose from the available tasks")
            return

        incomplete_tasks[task_number - 1]["completed"] = True
        print("Task marked completed")
    except:
        print("Invalid input, please enter a number")
        
           
def view_tasks(tasks):
    if not tasks:
        print("No tasks to view")
        return
    

    for i in tasks:
        if not isinstance(i["date"], datetime.datetime):
            i["date"] = datetime.datetime.strptime(i["date"], "%Y-%m-%d")
    
    print(f"Tasks:\n{'-' * 40}")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✕"
        print(f"{i}. {task['task']} ({task['date'].strftime('%Y-%m-%d')}) {status}")
    print("-" * 40)


if __name__ == "__main__":
    main(tasks)