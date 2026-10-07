# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

## Identitas

**Nama:** Aulia Nurrizqi  
**NIM:** 2225250160
**Kelas:** 3A
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika  
**Fakultas:** FKIP  
**Universitas:** Universitas Sultan Ageng Tirtayasa (UNTIRTA)  
**Pertemuan:** 06  

---

## Tujuan

Pada pertemuan ini, saya mempelajari dan mempraktikkan:

- Nested loop menggunakan Python.
- Pembuatan pola menggunakan loop baris dan kolom.
- Akumulasi nilai per baris.
- Akumulasi nilai secara keseluruhan.
- Pencacahan menggunakan counter.
- Penggunaan kondisi `if` di dalam nested loop.
- Tracing dua variabel kontrol, yaitu `i` dan `j`.
- Pengujian program menggunakan beberapa test case.
- Pengelolaan program menggunakan Git dan GitHub.

---

## Materi

Materi yang dipelajari pada Pertemuan 06 meliputi:

1. Nested Loop
2. Pola Baris dan Kolom
3. Pola Segitiga
4. Akumulasi Bertingkat
5. Pencacahan dengan Kondisi
6. Efisiensi Nested Loop
7. Debugging di VS Code
8. Git dan GitHub

---

## Struktur Folder

```text
pertemuan-06-nested-loop-NIM/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
│
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

---

# Latihan

## 1. Pasangan Indeks

File:

```text
latihan/01_pasangan_indeks.py
```

Program digunakan untuk menampilkan seluruh pasangan `(i, j)` dengan:

- `i = 1 sampai 3`
- `j = 1 sampai 4`

Loop luar digunakan untuk mengatur nilai `i`, sedangkan loop dalam digunakan untuk mengatur nilai `j`.

Jumlah pasangan yang dihasilkan:

```text
3 × 4 = 12 pasangan
```

Hasil akhir program:

```text
Banyak pasangan = 12
```

---

## 2. Pola Segitiga

File:

```text
latihan/02_pola_segitiga.py
```

Program menerima nilai `n` dan menghasilkan pola bintang.

Contoh untuk:

```text
n = 5
```

Output:

```text
* 
* * 
* * * 
* * * * 
* * * * *
```

Loop luar menentukan jumlah baris, sedangkan loop dalam menentukan jumlah bintang pada setiap baris.

---

## 3. Jumlah Per Baris

File:

```text
latihan/03_jumlah_per_baris.py
```

Program menghitung nilai `i × j` untuk:

```text
i = 1 sampai 4
j = 1 sampai 3
```

Hasil:

```text
Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
Jumlah baris 4 = 24
```

`total_baris` direset pada setiap iterasi loop luar karena jumlah yang dihitung adalah jumlah untuk setiap baris.

---

## 4. Menghitung Pasangan

File:

```text
latihan/04_hitung_pasangan.py
```

Program menghitung banyak pasangan `(i, j)` yang memenuhi kondisi:

```text
i + j <= n
```

Test case yang digunakan:

- `n = 2`
- `n = 3`
- `n = 5`

Program menggunakan `count` sebagai counter untuk menghitung banyak pasangan yang memenuhi kondisi.

---

# Tugas 3 - Tabel Perkalian dan Statistik

File:

```text
tugas/tabel_perkalian_dan_statistik.py
```

## Deskripsi

Program menerima sebuah bilangan bulat positif `n`.

Program kemudian:

1. Memvalidasi input `n`.
2. Membentuk tabel perkalian dari 1 sampai `n`.
3. Menghitung jumlah hasil perkalian pada setiap baris.
4. Menghitung jumlah seluruh hasil perkalian.
5. Menghitung banyak hasil perkalian yang bernilai genap.

---

## Algoritma

1. Meminta pengguna memasukkan nilai `n`.
2. Memeriksa apakah `n` lebih besar dari 0.
3. Jika `n <= 0`, pengguna diminta memasukkan kembali nilai `n`.
4. Menginisialisasi `total_semua = 0`.
5. Menginisialisasi `count_genap = 0`.
6. Menjalankan loop luar untuk `i` dari 1 sampai `n`.
7. Menginisialisasi `total_baris = 0` pada setiap baris.
8. Menjalankan loop dalam untuk `j` dari 1 sampai `n`.
9. Menghitung `hasil = i * j`.
10. Menampilkan hasil perkalian.
11. Menambahkan hasil ke `total_baris`.
12. Menambahkan hasil ke `total_semua`.
13. Memeriksa apakah hasil merupakan bilangan genap.
14. Jika hasil genap, `count_genap` ditambah 1.
15. Setelah loop dalam selesai, menampilkan jumlah baris.
16. Setelah seluruh loop selesai, menampilkan total keseluruhan dan jumlah hasil genap.

---

## Peran Variabel

### `i`

Digunakan sebagai variabel kontrol untuk **loop luar** dan mewakili baris tabel perkalian.

### `j`

Digunakan sebagai variabel kontrol untuk **loop dalam** dan mewakili kolom tabel perkalian.

### `hasil`

Menyimpan hasil perkalian:

```text
hasil = i × j
```

### `total_baris`

Digunakan sebagai akumulator untuk menghitung jumlah hasil perkalian pada setiap baris.

Variabel ini harus direset pada awal setiap iterasi loop luar.

### `total_semua`

Digunakan sebagai akumulator untuk menghitung jumlah seluruh hasil perkalian.

Variabel ini dibuat sebelum nested loop agar nilainya tidak kembali menjadi nol pada setiap baris.

### `count_genap`

Digunakan sebagai counter untuk menghitung banyak hasil perkalian yang bernilai genap.

---

# Cara Menjalankan Program

Pastikan Python sudah terpasang dan folder proyek sudah dibuka melalui VS Code.

Jalankan program utama dengan perintah:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

Pada beberapa sistem, perintah dapat menggunakan:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

---

# Hasil Pengujian

## Test Case 1

**Input:**

```text
n = 1
```

**Hasil yang diharapkan:**

```text
1
Total seluruh hasil = 1
Banyak hasil genap = 0
```

**Status:** Berhasil

---

## Test Case 2

**Input:**

```text
n = 2
```

**Tabel:**

```text
1    2
2    4
```

Jumlah baris:

```text
Jumlah baris 1 = 3
Jumlah baris 2 = 6
```

Total:

```text
Total seluruh hasil = 9
Banyak hasil genap = 3
```

**Status:** Berhasil

---

## Test Case 3

**Input:**

```text
n = 3
```

**Tabel:**

```text
1    2    3
2    4    6
3    6    9
```

Jumlah baris:

```text
Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
```

Total:

```text
Total seluruh hasil = 36
Banyak hasil genap = 5
```

**Status:** Berhasil

---

# Analisis Efisiensi

Pada program tugas, loop luar berjalan sebanyak `n` kali.

Loop dalam juga berjalan sebanyak `n` kali untuk setiap iterasi loop luar.

Oleh karena itu, badan loop dalam dijalankan sebanyak:

```text
n × n = n²
```

kali.

Contoh:

| n | Jumlah iterasi |
|---:|---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 10 | 100 |

Semakin besar nilai `n`, semakin banyak operasi yang dilakukan oleh nested loop.

---

# Refleksi

## 1. Mengapa `total_baris` direset pada setiap iterasi loop luar?

Karena `total_baris` digunakan untuk menghitung jumlah pada masing-masing baris. Jika tidak direset, jumlah dari baris sebelumnya akan ikut terbawa ke baris berikutnya.

## 2. Mengapa `total_semua` tidak direset pada setiap baris?

Karena `total_semua` digunakan untuk menghitung jumlah seluruh hasil perkalian. Oleh karena itu, nilainya harus terus bertambah sampai semua pasangan selesai diproses.

## 3. Berapa kali `hasil = i * j` dijalankan?

Untuk input `n`, pernyataan tersebut dijalankan sebanyak:

```text
n² kali
```

karena terdapat `n` iterasi pada loop luar dan `n` iterasi pada loop dalam.

## 4. Bagaimana membuktikan `count_genap` benar?

`count_genap` hanya ditambah satu ketika kondisi:

```python
hasil % 2 == 0
```

bernilai benar. Dengan demikian, hanya hasil perkalian yang genap yang dihitung.

## 5. Kesalahan yang ditemukan

Kesalahan yang perlu diperhatikan pada nested loop adalah salah menempatkan inisialisasi akumulator.

Contohnya, jika `total_semua = 0` diletakkan di dalam loop, nilainya akan terus direset sehingga tidak dapat menghitung total keseluruhan dengan benar.

Perbaikannya adalah menempatkan:

```python
total_semua = 0
```

sebelum nested loop.

---

# Kesimpulan

Pada Pertemuan 06, saya mempelajari penggunaan nested loop untuk memproses data dalam bentuk baris dan kolom. Saya juga mempelajari penggunaan akumulator untuk menjumlahkan nilai dan counter untuk menghitung banyaknya kejadian yang memenuhi kondisi.

Melalui tugas tabel perkalian dan statistik, saya dapat menerapkan nested loop, validasi input, akumulasi per baris, akumulasi keseluruhan, serta pencacahan hasil perkalian genap.

Saya juga belajar melakukan pengujian menggunakan beberapa test case serta mengelola hasil pekerjaan menggunakan Git dan GitHub.