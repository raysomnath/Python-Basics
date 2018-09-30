# You can update existing records in a table by using the "UPDATE" statement:

import sys
import mysql.connector

# Try connecting to database "mydatabase"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Somshona$1",
    database = "mydatabase", 
    auth_plugin = 'mysql_native_password'
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# To prevent SQL injection use below statements
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")