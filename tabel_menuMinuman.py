import mysql.connector

#tambahkan parameter database yang digunakan
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="menu"
)

cursor = db.cursor()
sql = """CREATE TABLE menuMinuman (
    nomor INT AUTO_INCREMENT PRIMARY KEY,
    nama_minuman VARCHAR(255),
    harga_minuman INT(255)
)
"""

cursor.execute(sql)

print("Tabel menuMinuman berhasil dibuat!")
