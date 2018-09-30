# You can check if a database exist by listing all tables in your database by using the "SHOW TABLES" statement:

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

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)