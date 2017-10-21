# python script to initialize database
import sqlite3

connection = sqlite3.connect('database.db')
print('Opened database successfully')

connection.execute('CREATE TABLE reminders (day TEXT, remind TEXT)')
print('Table created successfully')

connection.close()