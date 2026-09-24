# File: latihan/02_kategori_bilangan.py

x = int(input("Masukkan bilangan bulat: "))

if x < 0:
    print("Bilangan negatif")
elif x == 0:
    print("Nol")
elif x % 2 == 0:
    print("Bilangan positif genap")
else:
    print("Bilangan positif ganjil")