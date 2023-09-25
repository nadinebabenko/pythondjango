import mysql.connector     
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="070894",
) #

cursorObject =  database.cursor()
cursorObject.execute("CREATE DATABASE  giftsnew")
print("Database created")