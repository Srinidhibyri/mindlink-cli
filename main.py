from datetime import datetime        
        
tasks = []        
memoryNotes = {}        
todayPlan = []        
        
# (Load functions)        
        
def loadTasks():        
    try:        
        with open("tasks.txt", "r") as file:        
            for line in file:        
                parts = line.strip().split("|")        
                if len(parts) == 3:        
                    name, deadline, priority = parts        
                    tasks.append({        
                        "Name": name,        
                        "deadline": deadline,        
                        "priority": priority        
                    })        
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
        
# (Save functions)        
        
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
        
#(Task Functions)        
        
def addTask():        
    print("\nLet's add a new task")        
        
    name = input("Task name: ").strip()                
    if name == "":                
        print("Hmm... task cannot be empty")                
        return                
            
    deadline = input("Deadline (YYYY-MM-DD HH:MM): ").strip()                
    priority = input("Priority (High/Medium/Low): ").capitalize()                
            
    if priority not in ["High", "Medium", "Low"]:                
        print("Not sure abt that priority, setting it to Low")                
        priority = "Low"                
            
    try:                
        now = datetime.now()                
        task_time = datetime.strptime(deadline, "%Y-%m-%d %H:%M")                
            
        if task_time < now:                
            print("This deadline has already passed, but I'll still save it for you")                
    except:                
        print("That date format looks off. Try YYYY-MM-DD HH:MM")                
        return                
            
    tasks.append({                
        "Name": name,                
        "deadline": deadline,                
        "priority": priority                
    })                
            
    saveTasks()                
    print("Task added Successfully")        
        
def viewTasks():        
    if len(tasks) == 0:        
        print("\nNo tasks for now")        
        return        
        
    print("\nHere we go:")                
            
    for i in range(len(tasks)):                
        print(i+1, "-", tasks[i]["Name"], "| Deadline:", tasks[i]["deadline"], "| Priority:", tasks[i]["priority"])        
        
def deleteTask():        
    viewTasks()        
    if len(tasks) == 0:        
        return        
        
    try:                
        num = int(input("\nWhich task number should I remove? "))                
        if 1 <= num <= len(tasks):                
            tasks.pop(num-1)                
            saveTasks()                
            print("Done. Task removed")                
        else:                
            print("That number doesn't exist")                
    except:                
        print("That didn't look like a number")        
        
# (Memory)        
        
def memoryNote():        
    print("\nTell me what note ?")        
        
    item = input("Item: ").lower().strip()                
    loc = input("Where is it kept: ").strip()                
            
    memoryNotes[item] = loc                
    saveMemory()                
            
    print("Got it. I'll note that")        
        
def viewMemoryNotes():        
    if len(memoryNotes) == 0:        
        print("No memory notes yet")        
        return        
        
    print("\nHere is what I remember:")                
    for item in memoryNotes:                
        print(item, "is in", memoryNotes[item])        
        
def searchMemory():        
    item = input("What are you looking for: ").lower()        
    print(memoryNotes.get(item, " Sorry :( , I couldn't find that"))        
        
# -------- TODAY PLAN --------        
        
def addTodayPlan():        
    plan = input("What is the plan for today ?: ").strip()        
        
    if plan == "":                
        print("An empty plan won't help much")                
        return                
            
    todayPlan.append(plan)                
    savePlan()                
            
    print("Added to today's plan")        
        
def viewTodayPlan():        
    if len(todayPlan) == 0:        
        print("Nothing planned for today, we'll chill today")        
        return        
        
    print("\nToday's plan:")                
    for i in range(len(todayPlan)):                
        print(i+1, "-", todayPlan[i])        
        
def deletePlan():        
    viewTodayPlan()        
    if len(todayPlan) == 0:        
        return        
        
    try:                
        num = int(input("Which plan should I remove: "))                
        if 1 <= num <= len(todayPlan):                
            todayPlan.pop(num-1)                
            savePlan()                
            print("Removed from today's plan")                
        else:                
            print("That number doesn't exist")                
    except:                
        print("That didn't look like a number")        
        
# (MAIN)        
        
loadTasks()        
loadMemory()        
loadPlan()        
        
print("\n==============================")    
print(" Welcome to my 2nd Project: MINDLINK CLI")    
print("==============================")    
    
print("\nHey there! Really glad you're here ")    
    
print("\nIntroducing Linky...")    
print("Your External Memory Assistant ")    
    
print("\nFrom now on, I’ll take care of everything…")
print("we've 10 options given below... what do you want to choose?")
     
while True:        
    print("\n")        
        
    print("1. Add Task")                
    print("2. View Tasks")                
    print("3. Delete Task")                
    print("4. Add Memory Note")                
    print("5. View Memory Notes")                
    print("6. Search Memory")                
    print("7. Add Today Plan")                
    print("8. View Today Plan")                
    print("9. Delete Today Plan")                
    print("10. Exit")                
            
    choice = input("\nWhat would you like to do: ")                
            
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
        print("\nThank you for using me. Your External Memory Assistant Linky, will always be there for you !! ")                
        print("Thank you for using Mindlink :)")                
        break                        
    else:              
        print("Please select a valid option (1-10)")