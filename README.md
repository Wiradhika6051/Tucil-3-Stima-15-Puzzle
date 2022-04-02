# Tucil-3-Stima-15-Puzzle
Tucil 3 IF2211 dengan algoritma Branch &amp; Bound
Sebuah program untuk menyelesaikan permainan 15 Puzzle

# Identitas Author
- Nama: Fawwaz Anugrah Wiradhika Dharmasatya
- NIM:13520086
- Jurusan:Teknik Informatika

# Daftar Isi
1. [Deskripsi Singkat](#deskripsi-singkat)
2. [Requirement dan Instalasi](#requirement-dan-instalasi)
3. [Cara Penggunaan](#cara-penggunaan)
   - [Troubleshooting](#troubleshooting)
   - [Tambahan](#tambahan)

# Deskripsi Singkat
15 Puzzle adalah sebuah permainan dimana terdapat sebuah matriks 4x4 yang berisi angka 1-15 dan sebuah sel kosong yang tersusun secara acak. Tujuan permainan ini adalah menggerakkan sel-sel disekitar sel kosong agar terbentuk susunan akhir seperti berikut:
-`1  2  3  4`
-`5  6  7  8`
-`9  10 11 12`
-`13 14 15   `

Program ini adalah sebuah program dalam bahasa Python yang mencoba menyelesaikan puzzle ini dengan membangkitkan node-node dengan cara "menggerakkan" kotak kosong dan menghitung costnya. Jika seudah ditemukan solusi, maka simpul aktif yang costnya lebih besar dari cost solusi akan dipangkas.

# Requirement dan Instalasi
- Untuk dapat menjalankan aplikasi ini, pastikan terdapat Python 3.0
- Modul eksternal yang perlu disediakan:
  1.tkinter
  2.random
  3.os
  4.time
  5.threading
  6.copy
  7.operator
  penginstalan  modul dapat dilakukan dengan memasukkan command `pip install <nama-modul>`

# Cara Penggunaan
 1. Jalankan **main.py**
 2. Setelah GUI muncul, piih jenis input yang diinginkan di bawah label "Pilih Input"
    - Jika ingin program menghasilkan matriks sendiri, tekan tombol **GENERATE**. Akan terbentuk sebuah matriks acak secara otomatis.
    - Jika ingin memasukkan input matriks dari file eksternal, tekan tombol **CHOOSE FROM FILE**, lalu pilih file input. Setelah itu, tekan Open.
 3. Tekan tombol **SOLVE**.
 4. Tunggu hingga proses kelar dan menampilkan matriks akhir, total simpul, dan waktu pengerjaan.
 5. Pada matriks akhir, terdapat tombol **PREV MOVE** dan **NEXT MOVE**. Kedua tombol ini bertujuan untuk melihat langkah-per-langkah penyelesaian puzzle.
 

 ## Troubleshooting
 - Jika program not responding, maka ditunggu saja mengingat algoritma ini cukup berat untuk puzzle yang memerlukan move diatas 20 moves.
 ## Tambahan
 - Format penulisan input berupa matriks 4x4 dengan tiap elemen dipisahkan spasi dan untuk sel kosong, direpresentasikan sebagai nomor 16. Contoh:
`
5 2 8 10
1 11 6 4
7 9 16 3
13 14 15 12
`
 - Di repo ini, terdapat branch bernama **cli** yang berisi program yang sama namun dalam format CLI (command line interface). Algoritma yang digunakan sama dengan yang di branch ini. Saya menyertakannya karena awalnya saya membuat program ini dalam CLI untuk testing kemudian switch ke GUI. Karena sayang jika dihapus, saya masukkan program CLI nya ke branch yang berbeda.
