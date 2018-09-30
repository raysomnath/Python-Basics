# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

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

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for result in myresult:
    print(result)