import sys
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", 
    user= "root",
    password='Somshona$1',
    auth_plugin = 'mysql_native_password'
)
print(mydb)