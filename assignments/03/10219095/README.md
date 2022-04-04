# assignment 03
Terdapat kode Python berikut ini yang akan digunakan.
```python
import html
char1 = html.unescape('&#x25FB;')
char2 = html.unescape('&#x25FC;')

NIM = '10298345'
for x in NIM:
  n = int(x, 10)
  s = ''
  for i in range(n):
    s += char
  print(n, ':', s, sep='')
```

## question 1
Ganti nilai variabel NIM dengan data Anda, jalankan kode yang diberikan, dan tampilkan hasilnya.

### anwser 1
Hasil kode di atas adalah
```
Traceback (most recent call last):
  File "script1.py", line 10, in <module>
    s += char
NameError: name 'char' is not defined
```
Tested at OneCompailer [3xy53u8ng](https://onecompiler.com/python/3xy53u8ng)

## question 2
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char1`, jalankan dan tampilkan hasilnya.

### anwser 2
Hasil modifikasi kode di atas adalah
```
1:◻
0:
2:◻◻
1:◻
9:◻◻◻◻◻◻◻◻◻
0:
9:◻◻◻◻◻◻◻◻◻
5:◻◻◻◻◻
```
Tested at OneCompailer [3xy542h5c](https://onecompiler.com/python/3xy542h5c)

## question 3
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char2`, jalankan dan tampilkan hasilnya.

### anwser 3
Hasil modifikasi kode di atas adalah
```
1:◼
0:
2:◼◼
1:◼
9:◼◼◼◼◼◼◼◼◼
0:
9:◼◼◼◼◼◼◼◼◼
5:◼◼◼◼◼
```
Tested at OneCompailer [3xy548x7d](https://onecompiler.com/python/3xy548x7d)

## question 4
Jelaskan dengan singkat hal yang dihasillkan oleh kode yang diberikan.

### answer 4
Kode di atas berfungsi untuk
+ Merepresentasikan unicode hasil visualisasi dari NIM, dengan char1 berupa kotak kosong dan char2 berupa kotak berwarna
