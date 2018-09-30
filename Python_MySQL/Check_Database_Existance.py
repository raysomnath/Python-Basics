import sys
import mysql.connector

# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Somshona$1',
    auth_plugin = 'mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)