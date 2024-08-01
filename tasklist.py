tasks = []

def displaymenu():
    print("\nTo-Do List Manager")
    print("1. Show To-Do List")
    print("2. Add New Task")
    print("3. Complete a Task")
    print("4. Modify a Task")
    print("5. Remove a Task")
    print("6. Exit")

def showtasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks):
            completion = "Done" if task['done'] else "Pending"
            print(f"{index + 1}. {task['description']} - {completion}")

def createtask():
    taskdescription = input("Enter task description: ")
    tasks.append({'description': taskdescription, 'done': False})
    print("Task created!")

def completetask():
    showtasks()
    number = int(input("Select task number to complete: "))
    if 0 < number <= len(tasks):
        tasks[number - 1]['done'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def modifytask():
    showtasks()
    number = int(input("Select task number to modify: "))
    if 0 < number <= len(tasks):
        updateddescription = input("Enter updated description: ")
        tasks[number - 1]['description'] = updateddescription
        print("Task modified!")
    else:
        print("Invalid task number.")

def removetask():
    showtasks()
    number = int(input("Select task number to remove: "))
    if 0 < number <= len(tasks):
        tasks.pop(number - 1)
        print("Task removed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        displaymenu()
        userchoice = input("Choose an action: ")
        if userchoice == '1':
            showtasks()
        elif userchoice == '2':
            createtask()
        elif userchoice == '3':
            completetask()
        elif userchoice == '4':
            modifytask()
        elif userchoice == '5':
            removetask()
        elif userchoice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()