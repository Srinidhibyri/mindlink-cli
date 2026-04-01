tasks = []
memoryNotes = {}

def addTask():
    task = input("Add a task: ").strip()
    if task == "":
        print("Task cannot be empty!")
        return
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
            print(i+1, "-", tasks[i])

def searchMemory():
    item = input("Enter item to search: ").lower()
    if item in memoryNotes:
        print(f"{item} is in {memoryNotes[item]}")
    else:
        print("Item not found")

while True:
    print("\n==============================")
    print("Welcome to MINDLINK CLI")
    print("==============================")

    print("1. Add Task")
    print("2. Save Memory Note")
    print("3. View Tasks")
    print("4. Search Memory")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1": addTask()
    elif choice == "2": memoryNote()
    elif choice == "3": viewTasks()
    elif choice == "4": searchMemory()
    elif choice == "5":
        print("Thank you : )")
        break
    else:
        print("Invalid choice")
