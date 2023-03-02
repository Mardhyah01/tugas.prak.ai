nilai = float(input("Masukkan nilai ujian: "))

if nilai >= 90:
    hasil = "A"
    penjelasan = "Sangat baik, kamu benar-benar menguasai materi."
elif nilai >= 80:
    hasil = "B"
    penjelasan = "Baik, kamu cukup menguasai materi."
elif nilai >= 70:
    hasil = "C"
    penjelasan = "Cukup, kamu masih perlu meningkatkan pemahamanmu."
elif nilai >= 60:
    hasil = "D"
    penjelasan = "Kurang, kamu perlu belajar lebih giat lagi."
else:
    hasil = "E"
    penjelasan = "Sangat kurang, kamu harus serius belajar dan memperbaiki diri."

print("Hasil nilai ujian kamu adalah", hasil)
print(penjelasan)
