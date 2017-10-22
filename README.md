# remindme
RemindMe! An application that allows users to designate daily reminders that are emailed daily at their chosen time. 

If you clone this, change MY_ADDRESS and PASSWORD in sender.py to valid outlook login. Also change BTC amount in btc.py for personal amount. Changing these features in a clean & precise method through the program is in progress.

AFTER CHANGING ABOVE:

After cloning run: $ python3 initdb.py

After initializing database, run $ python3 main.py
  - Input all dates and reminders for the current week

Then schedule through cron or similar timing processes sender.py and send every day as seen fit. 

Support for sending repetively and changing software in place is in progress. This project is/was originally for private and personal use. Any questions feel free to email me : conner.bean1996@gmail.com
