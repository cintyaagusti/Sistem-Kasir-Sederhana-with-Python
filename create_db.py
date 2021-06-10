import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

#untuk mengeksekusi perintah sql atau query
cursor = db.cursor()
cursor.execute("CREATE DATABASE menu")

print("Database berhasil dibuat!")

