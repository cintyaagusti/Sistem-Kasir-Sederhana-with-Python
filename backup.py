print("-------7 DREAM CAFE-------")

pembeli = input("")
print("Nama Pembeli :", pembeli)

total1 = 0
jenis1 = ""
gelas = 0

def pilihanminuman():
    global total1
    global jenis1
    global gelas
    print("\nMenu Minuman :")

    menuMinuman = (
        '1. Watermark Juice - Rp23000',
        '2. Teanjun         - Rp22000',
        '3. Jeno Latte      - Rp22000',
        '4. Fullsun Ade     - Rp22000',
        '5. Namericano      - Rp22000',
        '6. Cherry Squash   - Rp21000',
        '7. Cola Park       - Rp20000')
    for minuman in menuMinuman:
        print(minuman)

    pilihan = int(input("Pilihan Minuman : "))
    gelas   = int(input("Jumlah Minuman  : "))

    if pilihan == 1:
        total1 = gelas * 23000
        print(gelas, "Watermark Juice = Rp", total1)
        jenis1 = ("Watermark Juice")
    elif pilihan == 2:
        total1 = gelas * 22000
        print(gelas, "Teanjun = Rp", total1)
        jenis1 = ("Teanjun")
    elif pilihan == 3:
        total1 = gelas * 22000
        print(gelas, "Jeno Latte = Rp", total1)
        jenis1 = ("Jeno Latte")
    elif pilihan == 4:
        total1 = gelas * 22000
        print(gelas, "Fullsun Ade = Rp", total1)
        jenis1 = ("Fullsun Ade")
    elif pilihan == 5:
        total1 = gelas * 22000
        print(gelas, "Namericano = Rp", total1)
        jenis1 = ("Namericano")
    elif pilihan == 6:
        total1 = gelas * 21000
        print(gelas, "Cherry Squash = Rp", total1)
        jenis1 = ("Cherry Squash")
    elif pilihan == 7:
        total1 = gelas * 20000
        print(gelas, "Cola Park = Rp", total1)
        jenis1 = ("Cola Park")
    else:
        print("Pilihan tidak tersedia, silahkan pesan menu lainnya.")
        pilihanminuman()

pilihanminuman()

total2 = 0
jenis2 = ""
porsi = 0

def pilihanmakanan():
    global total2
    global jenis2
    global porsi
    print("\nMenu Makanan :")

    menuMakanan = (
        '1. Cheese Cake     - Rp20000',
        '2. Banana Muffin   - Rp10000',
        '3. Tiramisu        - Rp15000',
        '4. Matcha Fudge    - Rp25000',
        '5. Choco Lava      - Rp15000')
    for makanan in menuMakanan:
        print(makanan)

    pilihan = int(input("Pilihan Makanan : "))
    porsi   = int(input("Jumlah Makanan  : "))

    if pilihan == 1:
        total2 = porsi * 20000
        print(porsi, "Cheese Cake = Rp", total2)
        jenis2 = ("Cheese Cake")
    elif pilihan == 2:
        total2 = porsi * 10000
        print(porsi, "Banana Muffin = Rp", total2)
        jenis2 = ("Banana Muffin")
    elif pilihan == 3:
        total2 = porsi * 15000
        print(porsi, "Tiramisu  = Rp", total2)
        jenis2 = ("Tiramisu")
    elif pilihan == 4:
        total2 = porsi * 25000
        print(porsi, "Matcha Fudge = Rp", total2)
        jenis2 = ("Matcha Fudge")
    elif pilihan == 5:
        total2 = porsi * 15000
        print(porsi, "Choco Lava  = Rp", total2)
        jenis2 = ("Choco Lava")
    else:
        print("Pilihan tidak tersedia, silahkan pesan menu lainnya.")
        pilihanmakanan()

pilihanmakanan()

totalsemua = 0
totalsemua = total1 + total2
print("\nSUBTOTAL: Rp", totalsemua)

uang = int(input("CASH: Rp "))
kembalian = int(uang - totalsemua)
print("KEMBALI: Rp", kembalian)



print("\n============================================")
print("======= S T R U K  P E M B E L I A N =======")
print("============================================")
print(" NAMA        :", pembeli)
print(" PEMBELIAN   :", porsi, jenis1, "-", total1)
print("              ", gelas, jenis2, "-", total2)
print(" SUBTOTAL    : Rp", totalsemua)
print(" CASH        : Rp", uang)
print(" KEMBALI     : Rp", kembalian)
print("\nTerima Kasih, Silahkan Datang Kembali")
print("============================================")
