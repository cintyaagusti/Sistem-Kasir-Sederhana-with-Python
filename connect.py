#untuk membuat koneksi ke mysql
import mysql.connector

#parameter jika menggunakan xampp
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

#mengecek status koneksi
if db.is_connected():
  print("Berhasil terhubung ke database")


