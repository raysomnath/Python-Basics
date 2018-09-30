# You can delete records from an existing table by using the "DELETE FROM" statement:

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

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")