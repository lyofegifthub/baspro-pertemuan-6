### Program Penjumlahan Matriks 5x5

Program ini dibuat untuk menghitung hasil penjumlahan dua buah matriks berukuran 5x5 menggunakan bahasa pemrograman Python.

---

## Deskripsi

Program akan melakukan penjumlahan matriks A dan B secara manual (tanpa menggunakan library seperti NumPy), lalu menyimpan hasilnya di matriks hasil, dan menampilkannya ke layar.

---

## Input

Dua buah matriks 5x5:

- Matriks A berisi angka-angka yang telah ditentukan.
- Matriks B juga berisi angka-angka yang telah ditentukan.

### Contoh:

python
A = [
    [30, 2, 3, 4, 5],
    [6, 26, 8, 9, 10],
    [11, 12, 13, 14, 7],
    [16, 17, 18, 19, 1],
    [21, 22, 23, 24, 31],
]

B = [
    [2, 3, 4, 5, 6],
    [15, 16, 17, 18, 19],
    [100, 101, 102, 103, 104],
    [25, 26, 27, 28, 29],
    [29, 30, 31, 32, 33],
]


---

## Cara Kerja Kode

### Inisialisasi Fungsi Penjumlahan

python
def add_matrices(A, B):
    result = []


Penjelasan:
Membuat fungsi add_matrices() yang menerima dua parameter: A dan B. Di dalam fungsi, dibuat list kosong result untuk menampung hasil akhir penjumlahan.

---

### Perhitungan Elemen Matriks

python
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


Penjelasan:
- i digunakan untuk iterasi baris.
- j digunakan untuk iterasi kolom.
- Elemen pada posisi [i][j] dari matriks A dan B dijumlahkan, lalu ditambahkan ke dalam list row.
- Setelah semua elemen pada satu baris dijumlahkan, row ditambahkan ke list result.

---

### Menampilkan Hasil

python
result = add_matrices(A, B)
for row in result:
    print(row)


Penjelasan:
- Fungsi add_matrices() dipanggil dan hasilnya disimpan di variabel result.
- Setiap baris dalam result dicetak satu per satu ke layar.

---

## Matriks Hasil

Contoh hasil output dari program (tergantung nilai matriks A dan B):


[32, 5, 7, 9, 11]
[21, 42, 25, 27, 29]
[111, 113, 115, 117, 111]
[41, 43, 45, 47, 30]
[50, 52, 54, 56, 64]
