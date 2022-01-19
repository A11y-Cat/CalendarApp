#------------Allisons calendar programme with category
import datetime

scheduleFile = "schedule.txt"
print("****Today's Tasks****".upper())

#------------opening schedule file

f = open(scheduleFile, "r")
MYSCHEDULE = f.read().split("\n")

#------------getting the date 

now = datetime.datetime.now()

#converting to a string I can use

todaysDate = now.strftime("%d-%m-%Y")

#printing string I can use

print("Todays date is " + str(todaysDate))

f.close()

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
        
#------------Asks for user input   
     
date = input("Input task due date (dd-mm-yyyy): ")
task = input("Advise the task: ")
category = input("Urgent or not urgent: ")

#------------Checks if task is due today
    
if(todaysDate == date):
  print("Todays Tasks:".upper())
  print("")
  print(date + " " + task + " " +  category.upper())
else:
  print("")
  print("You have no tasks due today")