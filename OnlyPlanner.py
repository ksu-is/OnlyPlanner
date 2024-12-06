
# Sample task list for demonstration
tasks = []

def addTask():
    task = input("Enter your task: ")
    urgency = input("Is this task urgent? (yes/no): ").lower()
    importance = input("Is this task important? (yes/no): ").lower()
    category = input("Please enter a category for the task: ")
    tasks.append({
        "task": task,
        "urgency": urgency == "yes",
        "importance": importance == "yes",
        "category": category,
        "completed": False
    })
    print(f"Task '{task}' added with urgency '{urgency}' and importance '{importance}'.")

def listTasks():
    if not tasks:
        print("No tasks here!")  
    else:
        print("Current tasks:")    
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} (Urgent: {task['urgency']}, Important: {task['importance']}, "
                  f"Category: {task['category']}, Status: {status})")

def eisenhowerSort():
    if not tasks:
        print("No tasks to sort.")
        return

    print("\nEisenhower Matrix:")
    categories = {
        "Urgent & Important": [],
        "Not Urgent but Important": [],
        "Urgent but Not Important": [],
        "Not Urgent & Not Important": []
    }

    for task in tasks:
        if task["urgency"] and task["importance"]:
            categories["Urgent & Important"].append(task)
        elif not task["urgency"] and task["importance"]:
            categories["Not Urgent but Important"].append(task)
        elif task["urgency"] and not task["importance"]:
            categories["Urgent but Not Important"].append(task)
        else:
            categories["Not Urgent & Not Important"].append(task)

    for category, items in categories.items():
        print(f"\n{category}:")
        if items:
            for task in items:
                print(f"- {task['task']}")
        else:
            print("No tasks in this category.")

def markMultipleTasksCompleted():
    listTasks()
    try:
        num_to_complete = int(input("How many tasks do you want to mark as completed? "))
        for _ in range(num_to_complete):
            taskToComplete = int(input("Enter the number of the task to mark as completed: "))
            if 0 <= taskToComplete < len(tasks):
                tasks[taskToComplete]["completed"] = True
                print(f"Task #{taskToComplete} marked as completed.")
            else:
                print(f"Task #{taskToComplete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the Only Planner!")
    print("This app helps organize your tasks based on urgency and importance.")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("1. Add a new task")
        print("2. List current tasks")
        print("3. View tasks by Eisenhower Matrix")
        print("4. Mark tasks as completed")
        print("5. Quit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            listTasks()
        elif choice == "3":
            eisenhowerSort()
        elif choice == "4":
            markMultipleTasksCompleted()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye! :)")
