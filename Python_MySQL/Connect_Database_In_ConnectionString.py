import sys
import mysql.connector

# Try connecting to database "mydatabase"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Somshona$1",
    database = "mydatabase", #Database where connectoin is to be made
    auth_plugin = 'mysql_native_password'
)
print(mydb)