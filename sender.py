# Main sending file used for sending the reminders
# 
# Author: Conner S. Bean
#
import sqlite3, datetime, btc, smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
Message maker
Returns string that will be email body
'''
def MakeMessage(name, reminders):
    message = "Good Morning " + name + "!\n\n This is your reminder message. \n\n"

    message += btc.main() + "\n\n"
    
    if (len(reminders) == 0):
        message += "You have no reminders today. Enjoy your Day! \n"
    else:
        count = 1
        message += "Reminders: \n"
        for rem in reminders:
            message += "Reminder " + str(count) + ": " + rem[1] + "\n"
            count += 1

    message += "\n\n Sent by RemindMe! \n Created by C.S. Bean"
    return message


'''
Main function
Creates connection/server/message
Sends message and closes connections
Reads data from btc and database
'''
def main():
    MY_ADDRESS = "remindme_script@outlook.com"
    PASSWORD = "r3m1ndm3!"

    # Current date
    curr = str(datetime.datetime.now().month)
    curr += '-' + str(datetime.datetime.now().day) + '-'
    curr += str(datetime.datetime.now().year)

    # Create connection to database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()


    # SQL Command for pulling all reminders for current day
    sql = "SELECT * FROM reminders WHERE day=" + "'" + curr +"'"
    cursor.execute(sql)
    stuff = cursor.fetchall()


    # set up the SMTP server
    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']="beanconn@msu.edu"
    msg['Subject']="Reminder for " + curr

    message = MakeMessage("Conner", stuff)

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    server.send_message(msg)
    del msg

'''
Run if in main and called.
'''
if __name__ == "__main__":
    main()