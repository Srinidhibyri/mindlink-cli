from datetime import datetime

tasks = []
memoryNotes = {}
todayPlan = []


def loadTasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name, deadline, priority = parts
                    tasks.append({"Name": name, "deadline": deadline, "priority": priority})
    except:
        pass

def loadMemory():
    try:
        with open("memory.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    item, loc = parts
                    memoryNotes[item] = loc
    except:
        pass

def loadPlan():
    try:
        with open("today.txt", "r") as file:
            for line in file:
                todayPlan.append(line.strip())
    except:
        pass


def saveTasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task["Name"] + "|" + task["deadline"] + "|" + task["priority"] + "\n")

def saveMemory():
    with open("memory.txt", "w") as file:
        for item in memoryNotes:
            file.write(item + "|" + memoryNotes[item] + "\n")

def savePlan():
    with open("today.txt", "w") as file:
        for plan in todayPlan:
            file.write(plan + "\n")


def addTask():
    name = input("Enter task name: ").strip()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    tasks.append({"Name": name, "deadline": deadline, "priority": priority})
    saveTasks()

    print("Task added successfully!")

def viewTasks():
    if len(tasks) == 0:
        print("No tasks available")
        return

    print("\nTasks:")
    for i in range(len(tasks)):
        print(i+1, "-", tasks[i]["Name"], "| Deadline:", tasks[i]["deadline"], "| Priority:", tasks[i]["priority"])

def deleteTask():
    viewTasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            saveTasks()
            print("Task deleted!")
    except:
        print("Invalid input")


def memoryNote():
    item = input("Item: ").lower().strip()
    loc = input("Location: ").strip()

    memoryNotes[item] = loc
    saveMemory()

    print("Memory saved!")

def viewMemoryNotes():
    if len(memoryNotes) == 0:
        print("No memory notes")
        return

    print("\nMemory Notes:")
    for item in memoryNotes:
        print(item, "->", memoryNotes[item])

def searchMemory():
    item = input("Search item: ").lower()
    print(memoryNotes.get(item, "Not found"))


def addTodayPlan():
    plan = input("Enter today's plan: ").strip()
    if plan == "":
        print("Empty plan!")
        return

    todayPlan.append(plan)
    savePlan()
    print("Plan added!")

def viewTodayPlan():
    if len(todayPlan) == 0:
        print("No plans today")
        return

    print("\nToday Plans:")
    for i in range(len(todayPlan)):
        print(i+1, "-", todayPlan[i])

def deletePlan():
    viewTodayPlan()
    if len(todayPlan) == 0:
        return

    try:
        num = int(input("Enter number: "))
        if 1 <= num <= len(todayPlan):
            todayPlan.pop(num-1)
            savePlan()
            print("Plan removed!")
    except:
        print("Invalid input")


loadTasks()
loadMemory()
loadPlan()

print("Data loaded successfully")

while True:
    print("\n==============================")
    print("Welcome to MINDLINK CLI")
    print("==============================")

    print("1 Add Task")
    print("2 View Tasks")
    print("3 Delete Task")
    print("4 Add Memory")
    print("5 View Memory")
    print("6 Search Memory")
    print("7 Add Plan")
    print("8 View Plan")
    print("9 Delete Plan")
    print("10 Exit")

    choice = input("Enter choice: ")

    if choice == "1": addTask()
    elif choice == "2": viewTasks()
    elif choice == "3": deleteTask()
    elif choice == "4": memoryNote()
    elif choice == "5": viewMemoryNotes()
    elif choice == "6": searchMemory()
    elif choice == "7": addTodayPlan()
    elif choice == "8": viewTodayPlan()
    elif choice == "9": deletePlan()
    elif choice == "10":
        print("Thank you!")
        break
    else:
        print("Invalid choice")