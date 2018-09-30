# You can also select the records that starts, includes, or ends with a given letter or phrase.
# Use the %  to represent wildcard characters:
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

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
