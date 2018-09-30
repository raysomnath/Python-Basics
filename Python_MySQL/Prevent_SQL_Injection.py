# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# The mysql.connector module has methods to escape query values:
# Escape query values by using the placholder %s method:

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

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)