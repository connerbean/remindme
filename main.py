# Main file for RemindMe Application
# Users will run this, and input their data 
#  and store it in DB
# 
# After, we will use sender to schedule reminders
#
# \Author: Conner S. Bean
# circa October 2017

import sqlite3, datetime

# Current date formatting
curr = str(datetime.datetime.now().year)
curr += '-' + str(datetime.datetime.now().month) + '-'
curr += str(datetime.datetime.now().day)

# Connect to database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Output rules/regulations
print("Input Format: (Date) (Reminder)")
print("Enter q to quit")

userInput = input("Enter Date and Reminder: ")

# Run until quit command, taking user input and entering into DB
while (userInput != "q"):
    # Error check
    if (len(userInput.split()) < 2):
        print("Please enter Date followed by reminder.")

    else:
        inputDate = userInput.split()[0]    # get the input date as first token
        inputDate = inputDate.replace('/', '-')         # replace slashes with dashes to minimize error
        inputReminder = userInput[userInput.index(' ') + 1:]    # rest of line signifying the reminder

        # try to insert the data into the reminders database
        try:
            cursor.execute('INSERT INTO reminders (day, remind) VALUES (?,?)', (inputDate, inputReminder))
            connection.commit()
            message = "Added successfully under date: " + inputDate

        # if failed then report an error to user
        except:
            connection.rollback()
            message = "Something went wrong. Make sure only 2 parameters are passed\
            and that the first parameter is in valid date format (MM-DD-YYYY)"

        finally:
            print(message)

    userInput = input("Enter Date and Reminder: ")

connection.close()