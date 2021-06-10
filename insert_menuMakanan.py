import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="menu"
)

cursor = db.cursor()
sql = "INSERT INTO menuMakanan (nomor_makanan, nama_makanan, harga_makanan) VALUES (%s, %s, %s)"
values = [
    (1, "Cheese Cake", 20000),
    (2, "Banana Muffin", 10000),
    (3, "Tiramisu", 15000),
    (4, "Matcha Fudge", 25000),
    (5, "Choco Lava", 15000)
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))


