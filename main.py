tasks = []
memoryNotes = {}

def addTask():
    name = input("Enter task name: ").strip()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    task = {"Name": name, "deadline": deadline}
    tasks.append(task)

    print("Task added successfully!")

def memoryNote():
    item = input("Enter item name: ").lower().strip()
    loc = input("Enter location: ").strip()
    memoryNotes[item] = loc
    print("Memory note saved!")

def viewTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i+1, "-", tasks[i]["Name"], "| Deadline:", tasks[i]["deadline"])
        print()

def searchMemory():
    item = input("Enter item to search: ").lower().strip()
    print("Result:", memoryNotes.get(item, "Not found"))

while True:
    print("\n==============================")
    print("Welcome to MINDLINK CLI")
    print("==============================")

    print("\n1. Add Task")
    print("2. Save Memory Note")
    print("3. View Tasks")
    print("4. Search Memory")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        addTask()
    elif choice == "2":
        memoryNote()
    elif choice == "3":
        viewTasks()
    elif choice == "4":
        searchMemory()
    elif choice == "5":
        print("\nThank you for using Mindlink!")
        break
    else:
        print("Invalid choice, try again")