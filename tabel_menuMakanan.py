import mysql.connector

#tambahkan parameter database yang digunakan
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="menu"
)

cursor = db.cursor()
sql = """CREATE TABLE menuMakanan (
    nomor INT AUTO_INCREMENT PRIMARY KEY,
    nama_makanan VARCHAR(255),
    harga_makanan INT(255)
)
"""

cursor.execute(sql)

print("Tabel menuMakanan berhasil dibuat!")

