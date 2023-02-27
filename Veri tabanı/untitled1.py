

import sqlite3

connections = sqlite3.connect('chinook.db')

cursor = connections.execute("select * from customers where city = 'Berlin'")

for row in cursor:
    print("First Name = " +row[1])


