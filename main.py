tasks = []
memoryNotes = {}

def addTask():
    print("\nAdd New Task")
    name = input("Enter task name: ").strip()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    tasks.append({"Name": name, "deadline": deadline})
    print("Task added successfully!")

def viewTasks():
    if len(tasks) == 0:
        print("\nNo tasks available")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]['Name']} | Deadline: {tasks[i]['deadline']}")

def deleteTask():
    viewTasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed['Name']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

def memoryNote():
    print("\nSave Memory Note")
    item = input("Item: ").lower().strip()
    loc = input("Location: ").strip()

    if item == "" or loc == "":
        print("Item or location cannot be empty!")
        return

    memoryNotes[item] = loc
    print("Memory saved!")

def viewMemoryNotes():
    if len(memoryNotes) == 0:
        print("\nNo memory notes found")
    else:
        print("\nMemory Notes:")
        for item in memoryNotes:
            print(f"{item} → {memoryNotes[item]}")

def searchMemory():
    item = input("\nEnter item to search: ").lower().strip()
    print("Result:", memoryNotes.get(item, "Not found"))

while True:
    print("\n==============================")
    print("Welcome to MINDLINK CLI")
    print("Your External Memory Assistant")
    print("==============================")

    print("\nChoose an option:")
    print("1. Add Task")
    print("2. Save Memory")
    print("3. View Tasks")
    print("4. Search Memory")
    print("5. Delete Task")
    print("6. View Memory")
    print("7. Exit")

    ch = input("\nEnter your choice: ")

    if ch == "1": addTask()
    elif ch == "2": memoryNote()
    elif ch == "3": viewTasks()
    elif ch == "4": searchMemory()
    elif ch == "5": deleteTask()
    elif ch == "6": viewMemoryNotes()
    elif ch == "7":
        print("\nThank you for using Mindlink!")
        break
    else:
        print("Please choose a valid option (1-7)")