# assignment 03
Terdapat kode Python berikut ini yang akan digunakan.
```python
import html
char1 = html.unescape('&#x25FB;')
char2 = html.unescape('&#x25FC;')

NIM = '10219098'
for x in NIM:
  n = int(x, 10)
  s = ''
  for i in range(n):
    s += char
  print(n, ':', s, sep='')
```

## question 1
Ganti nilai variabel NIM dengan data Anda, jalankan kode yang diberikan, dan tampilkan hasilnya.

### answer 1
Hasil kode di atas adalah
![alt text](https://github.com/AldianNurAzmar/fi3201-01-2021-2/blob/main/assignments/03/10219098/computational%20physics_assignment%2003_char.png)

## question 2
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char1`, jalankan dan tampilkan hasilnya.

### answer 2
Hasil modifikasi kode di atas adalah
![alt_text](https://github.com/AldianNurAzmar/fi3201-01-2021-2/blob/main/assignments/03/10219098/computational%20physics_assignment%2003_char1.png)

## question 3
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char2`, jalankan dan tampilkan hasilnya.

### answer 3
Hasil modifikasi kode di atas adalah
![alt_text](https://github.com/AldianNurAzmar/fi3201-01-2021-2/blob/main/assignments/03/10219098/computational%20physics_assignment%2003_char2.png)

## question 4
Jelaskan dengan singkat hal yang dihasilkan oleh kode yang diberikan.

### answer 4
Kode di atas berfungsi untuk
+ Memvisualisasikan setiap karakter (angka) yang terdapat dalam NIM yang tertera dengan unicode tertentu,
+ lalu setiap karakter (angka) yang terdapat dalam NIM yang tertera merepresentasikan jumlah unicode yang akan ditampilkan pada setiap karakternya.
+ Jika karakter pertama pada NIM adalah angka '1', maka jumlah unicode yang akan ditampilkan hanya satu, lalu jika karakter kedua pada NIM adalah angka '0', maka tidak akan ada unicode yang ditampilkan pada keluarannya, dan seterusnya. 
