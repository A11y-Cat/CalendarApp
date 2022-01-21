#------------Allisons calendar programme with category
import datetime

scheduleFile = "schedule.txt"

#------------Introducing app

print("Allison's Calendar App".upper())
print("")
print("1. View Todays Tasks")
print("2. Add New Task")
print("")

#------------User input for action

user = input("Please choose option 1 or 2: ")
print("")

#------------getting the date 

now = datetime.datetime.now()

#------------converting to a string I can use

todaysDate = now.strftime("%d-%m-%Y")

if(user == "1"):
#------------opening schedule file
    f = open(scheduleFile, "r")
    MYSCHEDULE = f.read().split("\n")
    print("")
    print("****Today's Tasks****".upper())
    print("")
    print("Todays date is " + str(todaysDate))

#------------schedule processing

    for line in range(0, len(MYSCHEDULE)):
        #this is a string which represents the current line in the list
        currentLine = MYSCHEDULE[line]
        taskDate = currentLine.split(",")[0]
        if(taskDate == todaysDate):
            print(currentLine.split(",")[1])
            print("This task is " + currentLine.split(",")[2])
            print("")
            f.close()
            
#------------Adds new task   

if(user == "2"):
    date = input("Input task due date (dd-mm-yyyy): ")
    task = input("Advise the task: ")
    category = input("Urgent or not urgent: ")
    
#------------Opens file to add user input
    a = open(scheduleFile, "a")
    a.write("\n" + date + "," + task + "," + category)
    a.close()