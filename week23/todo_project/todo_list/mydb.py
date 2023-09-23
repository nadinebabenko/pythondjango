import mysql.connector     
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="070894",
) #

cursorObject =  database.cursor()
cursorObject.execute("CREATE DATABASE  todo_app_xpp")
print("Database created")