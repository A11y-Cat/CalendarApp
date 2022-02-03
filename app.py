#------------Allisons calendar programme with category
import datetime
import smtplib
import ssl
from email.message import EmailMessage

scheduleFile = "schedule.txt"

#------------Introducing app

print("")
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
    print("")
    print("To Do:".upper())
    success = False
    
#------------schedule processing
    
    for line in range(0, len(MYSCHEDULE)):
#------------this is a string which represents the current line in the list
        currentLine = MYSCHEDULE[line]
        taskDate = currentLine.split(",")[0]
        if(taskDate == todaysDate):
            success = True
            print("")
            print(currentLine.split(",")[1].capitalize() + (" - ") + ("This task is " + currentLine.split(",")[2]))
            print("")
            break
            if(success == True):
                break
                
#------------If there are no task due

    if(success == False):
        print("")
        print("You have no tasks due today")
        print("")  
        user = input("Would you like to add a task? Type 1(No) or 2(Yes): ")
        print("")   
        if user != "2":
            print("See you next time!")
     
                    
    f.close()
                
#------------Adds new task   


if(user == "2"):

#------------user inputs date and checks format

    while True:
        date = input("Input task due date (dd-mm-yyyy): ")
        try:
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            dates = date.strftime("%d-%m-%Y")
            break
        except:
            print("Please input date in dd-mm-yyyy format")
            
#------------ user inputs task     
      
    task = input("Advise the task: ")
    
#------------user inputs category
    while True:
        category = input("Urgent or not urgent: ")
        if category.lower() == "Urgent":
            break
        elif category.lower() == "not urgent":
            break
        else:
            print("Please categorise your task as urgent or not urgent")
            
#------------Opens file to add user input
    a = open(scheduleFile, "a")
    a.write("\n" + dates + "," + task + "," + category)
    a.close()
    print("")
    print("Task added to calendar".upper())

#------------If user task is due today print task list
    
    if(dates == todaysDate):
        f = open(scheduleFile, "r")
        MYSCHEDULE = f.read().split("\n")
        print("")
        print("****Today's Tasks****".upper())
        print("")
        print("Todays date is " + str(todaysDate))
        print("")
        print("To Do:".upper())

#------------If user adds task due today, shows task list

        for line in range(0, len(MYSCHEDULE)):
            #this is a string which represents the current line in the list
            currentLine = MYSCHEDULE[line]
            taskDate = currentLine.split(",")[0]
            if(taskDate == todaysDate):
                print("")
                print(currentLine.split(",")[1] + (" - ") + ("This task is " + currentLine.split(",")[2]))
                print("")
                f.close()
                
def sendEmail():
    subject = "Tasks Due Today"
    senderEmail = "c0d3ra11y@gmail.com"
    receiverEmail = "c0d3ra11y@gmail.com"
    password = input("Enter a password: ")

    message = EmailMessage()
    message["From"] = senderEmail
    message["To"] = receiverEmail
    message["Subject"] = subject
    body = cLine.split(",")[1] + (" - ") + ("this task is " + cLine.split(",")[2])
    message.set_content(body)

    context = ssl.create_default_context()

    print("sending email")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail,receiverEmail, message.as_string())
        
        print("email sent")
                
o = open(scheduleFile, 'r')
task = o.read().split("\n")

for line in range(0, len(task)):
    cLine = task[line]
    date = cLine.split(",")[0]
    if date == todaysDate:
        sendEmail()
        o.close()
                