# Start from position 3, and return 5 records:

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

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)