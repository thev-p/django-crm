import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

# preparing a cursor object
cursorObject = database.cursor()

# creating a database
# mysql database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")