# Kuis Formatif Pertemuan 06

## Nested Loop, Pola, Akumulasi, dan Pencacahan

**Nama:** Aulia Nurrizqi  
**NIM:** 2225250160
**Kelas:** 3A

---

### 1. Jika loop luar berjalan 4 kali dan loop dalam 6 kali, berapa total iterasi badan loop dalam?

**Jawaban:**  
4 × 6 = **24 iterasi**.

Jadi, total iterasi badan loop dalam adalah **24 kali**.

---

### 2. Kapan loop dalam kembali ke nilai awal?

**Jawaban:**  
Loop dalam kembali ke nilai awal setiap kali terjadi iterasi baru pada loop luar. Setelah loop dalam selesai, ketika nilai loop luar berubah, loop dalam akan dimulai kembali dari nilai awal sesuai dengan `range` yang digunakan.

---

### 3. Apa fungsi `print()` setelah loop dalam pada pola simbol?

**Jawaban:**  
`print()` setelah loop dalam berfungsi untuk **memindahkan output ke baris berikutnya**, sehingga setiap iterasi loop luar menghasilkan satu baris pola.

---

### 4. Di mana `total_baris` harus diinisialisasi jika jumlah dihitung untuk setiap baris?

**Jawaban:**  
`total_baris` harus diinisialisasi **di dalam loop luar dan sebelum loop dalam**.

Contoh:

```python
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        ...
```

---

### 5. Di mana `total_semua` harus diinisialisasi jika jumlah mencakup seluruh pasangan?

**Jawaban:**  
`total_semua` harus diinisialisasi **sebelum kedua loop dimulai**.

Contoh:

```python
total_semua = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        ...
```

---

### 6. Apa perbedaan counter dengan accumulator?

**Jawaban:**  
**Counter** digunakan untuk menghitung banyaknya kejadian atau pasangan yang memenuhi suatu kondisi.

Contoh:

```python
count += 1
```

Sedangkan **accumulator** digunakan untuk mengumpulkan atau menjumlahkan nilai secara bertahap.

Contoh:

```python
total += nilai
```

---

### 7. Jika i dan j dari 1 sampai 3, berapa pasangan yang diperiksa?

**Jawaban:**  

3 × 3 = **9 pasangan**.

Pasangan yang diperiksa adalah:

```text
(1,1), (1,2), (1,3)
(2,1), (2,2), (2,3)
(3,1), (3,2), (3,3)
```

Jadi, terdapat **9 pasangan** yang diperiksa.

---

### 8. Bagaimana `if` dapat digabung dengan nested loop untuk pencacahan?

**Jawaban:**  
`if` dapat diletakkan di dalam loop dalam untuk memeriksa setiap pasangan yang dihasilkan oleh nested loop. Jika pasangan memenuhi kondisi tertentu, counter ditambah 1.

Contoh:

```python
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1
```

---

### 9. Apa arti working tree clean pada `git status`?

**Jawaban:**  
`working tree clean` berarti **tidak ada perubahan file yang belum di-commit** pada working tree. Artinya, kondisi file lokal sudah sesuai dengan commit terakhir.

---

### 10. Perintah apa yang mengirim commit lokal terbaru ke GitHub?

**Jawaban:**  

```bash
git push
```

Perintah tersebut digunakan untuk mengirim commit lokal ke repositori GitHub.

---