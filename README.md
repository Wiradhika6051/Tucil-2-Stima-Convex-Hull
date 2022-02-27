# Tucil-2-Stima-Convex-Hull
Sebuah library yang bisa digunakan untuk mencari convex hull dari sebuah dataset

# Identitas Author
- Nama: Fawwaz Anugrah Wiradhika Dharmasatya
- NIM:13520086
- Jurusan:Teknik Informatika

# Daftar Isi
1. [Deskripsi Singkat](#deskripsi-singkat)
2. [Requirement dan Instalasi](#requirement-dan-instalasi)
3. [Cara Penggunaan](#cara-penggunaan)

# Deskripsi Singkat
*Convex Hull* adalah sebuah poligon terkecil yang melingkupi semua titik dalam suatu data. Library ini bertujuan untuk menghasilkan daftar pasangan titik yang membentuk *Convex Hull* searah jarum jam. Pembentukan pasangan titik ini dilakukan menggunakan strategi *Divide and Conquer*.

# Requirement dan Instalasi
- Untuk dapat menjalankan aplikasi ini, pastikan dulu Python sudah terinstall di perangkat.
- Dataset yang digunakan hanya bisa berupa CSV.
- Sudah terdapat modul numpy dan math di perangkat/kernel agar dapat menggunakan library. Jika ingin mencoba program di file main.py, pastikan juga terdapat modul pandas,matplotlib,serta sklearn (Untuk dapat menggunakan dataset contoh dari sklearn).
- Jika terdapat modul-modul diatas yang belum tersedia, modul tersebut dapat di-*install* menggunakan perintah berikut di shell:
    `pip install <nama-modul>`

# Cara Penggunaan
- Jika hanya ingin menggunakan library:
 1. import library menggunakan kode:
    `import myConvexHull`
 2. Sediakan dataset yang sudah dimuat dalam bentuk numpy array.
 3. Buat sebuah objek dari kelas **MyConvexHull** dengan parameter berupa data yang sudah dimuat. Contoh kode:
    `convex = myConvexHull.MyConvexHull(data)`
 4. Untuk dapat mendapatkan pasangan titik pembentuk *convex hull*, panggil atribut **simplices** di objek tersebut. Contoh:
    `convex_list = convex.simplices`
- Jika ingin mencoba program **main.py** di **src**:
 1. Jalankan file **main.py**.
 2. Masukkan pilihan sumber data yang diinginkan.
    - Jika memilih sumber data dari dataset sklearn:
      1. Masukkan nomor dataset yang ingin digunakan.
      2. Pilih nomor atribut yang ingin menjadi sumbu-x
      3. Pilih nomor atribut yang ingin menjadi sumbuu-y
      4. Hasil akhir berupa grafik *scatter* beserta *convex hull*.
    - Jika memilih sumber data dari file eksternal:
      1. Masukkan nama file tanpa format .csv. Pastikan dataset sudah ada di file test. Contoh:
      `air_polution`
      2. Pilih nomor atribut yang ingin menjadi sumbu-x
      3. Pilih nomor atribut yang ingin menjadi sumbuu-y
      4. Hasil akhir berupa grafik *scatter* beserta *convex hull*.