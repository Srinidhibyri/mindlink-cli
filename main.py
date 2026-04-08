from datetime import datetime

tasks = []
memoryNotes = {}
todayPlan = []


def addTask():
    print("\n Add New Task")
    name = input("Enter task name: ").strip()
    deadline = input("Enter deadline (YYYY-MM-DD): ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    tasks.append({"Name": name, "deadline": deadline})
    print("Task added!")

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
        num = int(input("\nEnter task number: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f" Deleted: {removed['Name']}")
        else:
            print("Invalid number")
    except:
        print("Enter valid number")


def memoryNote():
    print("\nSave Memory")
    item = input("Item: ").lower().strip()
    loc = input("Location: ").strip()

    if item == "" or loc == "":
        print("Cannot be empty")
        return

    memoryNotes[item] = loc
    print("Saved!")

def viewMemoryNotes():
    if len(memoryNotes) == 0:
        print("\nNo memory notes")
    else:
        print("\nMemory Notes:")
        for item in memoryNotes:
            print(f"{item} → {memoryNotes[item]}")

def searchMemory():
    item = input("\nSearch item: ").lower().strip()
    print("Result:", memoryNotes.get(item, "Not found"))



def addTodayPlan():
    print("\nAdd Today's Plan")
    plan = input("Enter plan: ").strip()

    if plan == "":
        print("Plan cannot be empty!")
        return

    todayPlan.append(plan)
    print("Plan added!")

def viewTodayPlan():
    if len(todayPlan) == 0:
        print("\nNo plans for today")
    else:
        print("\nToday's Plans:")
        for i in range(len(todayPlan)):
            print(f"{i+1}. {todayPlan[i]}")

def deletePlan():
    viewTodayPlan()
    if len(todayPlan) == 0:
        return

    try:
        num = int(input("\nEnter plan number: "))
        if 1 <= num <= len(todayPlan):
            removed = todayPlan.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")
    except:
        print("Enter valid number")


while True:
    print("\n==============================")
    print("Welcome to MINDLINK CLI")
    print("Your External Memory Assistant")
    print("==============================")

    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Save Memory")
    print("5. View Memory")
    print("6. Search Memory")
    print("7. Add Today Plan")
    print("8. View Today Plan")
    print("9. Delete Today Plan")
    print("10. Exit")

    ch = input("\nEnter your choice: ")

    if ch == "1": addTask()
    elif ch == "2": viewTasks()
    elif ch == "3": deleteTask()
    elif ch == "4": memoryNote()
    elif ch == "5": viewMemoryNotes()
    elif ch == "6": searchMemory()
    elif ch == "7": addTodayPlan()
    elif ch == "8": viewTodayPlan()
    elif ch == "9": deletePlan()
    elif ch == "10":
        print("\nThank you for using Mindlink!")
        break
    else:
        print("Choose valid option (1-10)")