# Inisialisasi variabel harga barang
harga_makanan = 15000
harga_minuman = 5000

# Meminta input dari pengguna mengenai jumlah barang yang dibeli
jumlah_makanan = int(input("Masukkan jumlah makanan yang dibeli: "))
jumlah_minuman = int(input("Masukkan jumlah minuman yang dibeli: "))

# Menghitung total harga sebelum pajak
total_sebelum_pajak = (harga_makanan * jumlah_makanan) + (harga_minuman * jumlah_minuman)

# Menghitung pajak sebesar 10% dari total harga sebelum pajak
pajak = 0.1 * total_sebelum_pajak

# Menghitung total harga setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

# Mencetak total harga, pajak, dan total harga setelah pajak
print("Total harga sebelum pajak: Rp", total_sebelum_pajak)
print("Pajak: Rp", pajak)
print("Total harga setelah pajak: Rp", total_setelah_pajak)

# Meminta input dari pengguna mengenai jumlah uang yang diberikan
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: "))

# Menghitung kembalian
kembalian = uang_diberikan - total_setelah_pajak

# Mencetak kembalian
print("Kembalian: Rp", kembalian)
