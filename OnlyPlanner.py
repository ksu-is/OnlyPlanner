#I added urgency and importance levels here
def addTask():
    task = input("Please enter a task: ")
    urgency = input("Is this task urgent? (yes/no): ").lower()
    importance = input("Is this task important? (yes/no): ").lower()
    category = input("Please enter a category or label for the task: ")
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
        print("There are no tasks currently.")  
        
        taskToDelete = int(input("Enter the number to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else: 
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid input.")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")  
    else:
        print("Current tasks:")    
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} (Priority: {task['priority']}, Category: {task['category']}, Status: {status})")


def prioritizeTask():
    listTasks()
    try:
        taskToPrioritize = int(input("Enter the number of the task to prioritize: "))
        if taskToPrioritize >=0 and taskToPrioritize < len(tasks):
            new_priority = input("Enter new priority (1 for high, 2 for medium, 3 for low): ")
            tasks[taskToPrioritize]["priority"] = new_priority
            print(f"Task #{taskToPrioritize} priority updated to {new_priority}.")
        else:
            print(f"Task #{taskToPrioritize} was not found")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid task number.")


def sortTasks():
    listTasks()
    try:
        sort_choice = input("Sort by (1. Priority, 2. Category): ")
        if sort_choice == "1":
            tasks.sort(key=lambda x: x["priority"])
            print("Tasks sorted by priority:")
            listTasks()
        elif sort_choice == "2":
            tasks.sort(key=lambda x: x["category"])
            print("Tasks sorted by category:")
            listTasks()
        else:
            print("Invalid choice.")
    except:
        print("Invalid input.")
#This can be a good addition. Notating the amount of tasks the user wants to complete.

def markTaskCompleted():
    listTasks()
    try:
        taskToComplete = int(input("Enter the number of the task to mark as completed: "))
        if  taskToComplete >=0 and taskToComplete < len(tasks):
            tasks[taskToComplete]["completed"] = True
            print(f"Task #{taskToComplete} marked as completed.")
        else:
            print(f"Task #{taskToComplete} was not found")
    except:
        print("Invalid input.")
        


if __name__ == "__main__":
    ### Create a loop to run the app
    print("Welcome to the TaskTrack App! :) You will be able to add, delete, list, prioritize tasks, sort tasks, mark tasks as completed, as well as exit the app when needed. After exiting, the choices will no longer appear, and the current data will not be saved, so please keep that in mind. The overall goal is to help users with their productivity.")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Prioritize task(s)")
        print("5. Sort tasks")
        print("6. Mark task as completed")
        print("7. Quit")

        choice = input("Enter your choice: ")
        
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTasks()
        elif(choice=="4"):
            prioritizeTask()
        elif(choice=="5"):
            sortTasks()
        elif(choice=="6"):
            markTaskCompleted()
        elif(choice=="7"):
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye! :)")
