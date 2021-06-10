import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="menu"
)

cursor = db.cursor()
sql = "INSERT INTO menuMinuman (nomor_minuman, nama_minuman, harga_minuman) VALUES (%s, %s, %s)"
values = [
    (1, "Watermark Juice", 23000),
    (2, "Teanjun", 22000),
    (3, "Jeno Latte", 22000),
    (4, "Fullsun Ade", 22000),
    (5, "Namericano", 22000),
    (6, "Cherry Squash", 21000),
    (7, "Cola Park", 20000)
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))


