import sys
import mysql.connector

# To create a database in MySQL, use the "CREATE DATABASE" statement

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Somshona$1',
    auth_plugin = 'mysql_native_password'
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")