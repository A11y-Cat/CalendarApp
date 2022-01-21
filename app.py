#------------Allisons calendar programme with category
import datetime

scheduleFile = "schedule.txt"


#------------opening schedule file

f = open(scheduleFile, "r")
MYSCHEDULE = f.read().split("\n")

#------------getting the date 

now = datetime.datetime.now()

#converting to a string I can use

todaysDate = now.strftime("%d-%m-%Y")

#------------Asks for user input   

date = input("Input task due date (dd-mm-yyyy): ")
task = input("Advise the task: ")
category = input("Urgent or not urgent: ")

a = open(scheduleFile, "a")
a.write("\n" + date + "," + task + "," + category)

f.close()
a.close()

print("")
print("")
print("****Today's Tasks****".upper())
print("")

#------------printing string I can use

print("Todays date is " + str(todaysDate))

#------------schedule processing

for line in range(0, len(MYSCHEDULE)):
    #this is a string which represents the current line in the list
    currentLine = MYSCHEDULE[line]
    taskDate = currentLine.split(",")[0]
    print("")
    if(taskDate == todaysDate):
        print(currentLine.split(",")[1])
        print("This task is " + currentLine.split(",")[2])
        print("")
        

