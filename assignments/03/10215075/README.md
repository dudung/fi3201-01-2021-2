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
  File "HelloWorld.py", line 10, in <module>
    s += char
NameError: name 'char' is not defined
```
Tested at OneCompiler [3xr4hufmm](https://onecompiler.com/python/3xr4hufmm)

## question 2
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char1`, jalankan dan tampilkan hasilnya.

### anwser 2
Hasil modifikasi kode di atas adalah
```
1:◻
0:
2:◻◻
1:◻
5:◻◻◻◻◻
0:
7:◻◻◻◻◻◻◻
5:◻◻◻◻◻
```
Tested at OneCompiler [3xr4j6uab](https://onecompiler.com/python/3xr4j6uab)

## question 3
Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan `s += char2`, jalankan dan tampilkan hasilnya.

### anwser 3
Hasil modifikasi kode di atas adalah
```
1:◼
0:
2:◼◼
1:◼
5:◼◼◼◼◼
0:
7:◼◼◼◼◼◼◼
5:◼◼◼◼◼
```
Tested at OneCompiler [3xr4jaz58](https://onecompiler.com/python/3xr4jaz58)

## question 4
Jelaskan dengan singkat hal yang dihasillkan oleh kode yang diberikan.

### answer 4
Kode di atas berfungsi untuk
+ `import html` berfungsi untuk memanggil file html.py
+ `char1 = html.unescape('&#x25FB;')` untuk mendefinisikan variabel char1 sebagai suatu objek dari file html yaitu &#x25FB;
+ `char2 = html.unescape('&#x25FC;')` untuk mendefinisikan variabel char2 sebagai suatu objek dari file html yaitu &#x25FC;
+ perintah `unescape()` digunakan untuk decode url yang ter-enkripsi ke bentuk semula. Dalam kode ini, `unescape('&#x25FB;')` mendecode `&#x25FB;` menjadi &#x25FB; sedangkan `unescape('&#x25FC;')` mendecode `&#x25FC;` menjadi &#x25FC; 
+ `NIM = '10298345'` untuk definisi variabel NIM sebagai `10298345`, yang nantinya diganti menjadi dengan data NIM masing-masing. contoh pada saya sehingga variabel NIM didefinisikan sebagai 10215075
+  `for x in NIM:
  n = int(x, 10)
  s = ''
  for i in range(n):
    s += char
  print(n, ':', s, sep='')
  ` 
+ `for` digunakan untuk looping dan `print` digunakan untuk mencetak. 
+ Dalam kode ini `for x in NIM:` looping dilakukan sebanyak x kali, yaitu sebanyak angka yang ada pada NIM. Karena NIM saya 10215075 maka fungsi akan looping sebanyak 8 kali. `n = int(x, 10)` untuk definisi variabel n sebagai bilangan integer x (0 hingga 9) dimana akan menghasilkan angka pertama dari NIM saya yaitu 1 pada loop pertama. `s = ''` untuk definisi variabel s sebagai kosong. 
+ kemudian `for i in range(n):` looping sebanyak i, yaitu sebanyak nilai n. `s += char` untuk definisi s sebagai variabel char sebanyak n. pada soal 1, karena variabel char tidak terdefinisi maka hasil akan eror. Pada soal 2, `s += char1` definisi variabel s sebagai char1 yaitu &#x25FB; sebanyak n.
+ `print(n, ':', s, sep='')` untuk mencetak argumen-argumen didalamnya dan `sep=''` digunakan agar argumen-argumen dicetak dengan separator, karena diisi kosong maka argumen dicetak tanpa separator. Setelah dicetak maka akan pindah baris baru dan setelahnya akan melakukan looping kedua yaitu dengan mencetak angka kedua dari NIM beserta kotak sebanyak angkanya dan seterusnya sampai mencetak angka terakhir dari NIM.

 
 
