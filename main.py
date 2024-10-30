# Daftar menu beserta harganya
menu = {
    1: ("Nasgor biasa", 15000),
    2: ("Nasgor Sosis", 17000),
    3: ("Nasgor Bakso", 17000),
    4: ("Nasgor Ati", 18000),
    5: ("Nasgor Spesial", 20000),
    6: ("Es teh/Teh anget", 3000),
    7: ("Es jeruk", 4000),
    8: ("Es campurdawet", 8000)
}

# Tampilkan menu
print("--Menu Nasgor Gila Parkur--\n")
print("Menu Makanan:")
for i in range(1, 6):
    print(f"{i}. {menu[i][0]} = Rp.{menu[i][1]:,}")

print("\nMenu Minuman:")
for i in range(6, 9):
    print(f"{i}. {menu[i][0]} = Rp.{menu[i][1]:,}")

# Inisialisasi total harga
total_harga = 0

# Meminta input pesanan
while True:
    try:
        pesanan = int(input("\nMasukan pesanan anda (0 untuk selesai): "))
        if pesanan == 0:
            break
        elif pesanan in menu:
            total_harga += menu[pesanan][1]
            print(f"{menu[pesanan][0]} ditambahkan dengan harga Rp. {menu[pesanan][1]:,}")
        else:
            print("Menu tidak ditemukan. Silakan masukkan nomor yang benar.")
    except ValueError:
        print("Masukkan nomor yang valid.")

# Tampilkan total harga
print(f"\nTotal harga pesanan anda = Rp. {total_harga:,}")
