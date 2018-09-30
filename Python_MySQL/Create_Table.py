# To create a table in MySQL, use the "CREATE TABLE" statement.

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

mycursor.execute("CREATE TABLE customers (name varchar(255), address VARCHAR(255))")
