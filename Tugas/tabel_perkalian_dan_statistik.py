print("Tabel Perkalian dan Statistik")

# Input dan validasi n
n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

# Inisialisasi akumulator dan counter
total_semua = 0
count_genap = 0

# Nested loop untuk membuat tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian
        print(f"{hasil:4}", end="")

        # Menghitung jumlah per baris dan keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Menghitung banyak hasil yang genap
        if hasil % 2 == 0:
            count_genap += 1

    # Menampilkan jumlah setiap baris
    print(f" | Jumlah baris = {total_baris}")

# Menampilkan hasil akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")