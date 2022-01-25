# Assignment 03

# Question 1
Terdapat kode Python berikut ini yang akan digunakan. Ganti nilai variabel NIM dengan data Anda, jalankan kode yang diberikan, dan tampilkan hasilnya.
```python
import html 
char1 = html.unescape('&#x25FB;') 
char2 = html.unescape('&#x25FC;') 
NIM = '10218009'
for x in NIM: 
  n = int(x, 10) 
  s = '' 
  for i in range(n): 
    s += char
  print(n, ':', s, sep='') 
  ```
  ## Answer 1
  ```
  NameError                                 Traceback (most recent call last)
<ipython-input-8-d14d2814d4c4> in <module>
      3   s = ''
      4   for i in range(n):
----> 5     s += char
      6   print(n, ':', s, sep='')

NameError: name 'char' is not defined
  ```
  Tested in python
  ![alt text](https://github.com/AkramAkbarAmin/fi3201-01-2021-2/blob/main/assignments/03/10218009_Assignment%203_Answer%20for%20question%201.png)
  
  # Question 2
  Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan s += char1, jalankan dan tampilkan hasilnya.
  ```python
  import html 
char1 = html.unescape('&#x25FB;') 
char2 = html.unescape('&#x25FC;') 
NIM = '10218009'
for x in NIM: 
  n = int(x, 10) 
  s = '' 
  for i in range(n): 
    s += char1 
  print(n, ':', s, sep='') 
  ```
  ## Answer 2
  ```
  1:◻
  0:
  2:◻◻
  1:◻
  8:◻◻◻◻◻◻◻◻
  0:
  0:
  9:◻◻◻◻◻◻◻◻◻
  ```
  Tested in python
  ![alt text](https://github.com/AkramAkbarAmin/fi3201-01-2021-2/blob/main/assignments/03/10218009_Assignment%203_Answer%20for%20question%202.png)
  
  # Question 3
Terdapat kode Python berikut ini yang akan digunakan. Ganti nilai variabel NIM dengan data Anda, modifikasi kode yang diberikan di atas dengan s += char2, jalankan dan tampilkan hasilnya.
```python
import html 
char1 = html.unescape('&#x25FB;') 
char2 = html.unescape('&#x25FC;') 
NIM = '10218009'
for x in NIM: 
  n = int(x, 10) 
  s = '' 
  for i in range(n): 
    s += char2 
  print(n, ':', s, sep='') 
  ```
  ## Answer 3
  ```
  1:◼
  0:
  2:◼◼
  1:◼
  8:◼◼◼◼◼◼◼◼
  0:
  0:
  9:◼◼◼◼◼◼◼◼◼
  ```
  Tested in python
  ![alt text](https://github.com/AkramAkbarAmin/fi3201-01-2021-2/blob/main/assignments/03/10218009_Assignment%203_Answer%20for%20question%203.png)
  
  # Question 4
  Jelaskan dengan singkat hal yang dihasillkan oleh kode yang diberikan.
  ## Answer 4
  ```python
import html #berfungsi untuk mengimport module html
char1 = html.unescape('&#x25FB;') #kode untuk kotak berwarna putih
char2 = html.unescape('&#x25FC;') #kode untuk kotak berwarna hitam
NIM = '10218010' #string dalam Python adalah array byte yang mewakili karakter unicode.
for x in NIM: #fungsi for mendefinisikan setiap x dalam variabel NIM
  n = int(x, 10) #transformasi integer dari setiap character NIM yang terhitung didalam x dan mengizinkan pembuatan kotak hingga 9
  s = '' #berfungsi mendefinisikan apa yang ditampilkan dari setiap karakter dalam NIM
  for i in range(n): #fungsi for
    s += char #s digunakan sebagai substitusi variabel baru berdasarkan kode html yang diberikan (+= berarti menjumlahkan variabel dan menjadikan nilai s bernilai sebesar hasil penjumlahan tersebut)
  print(n, ':', s, sep='') #hasilnya akan berupa setiap character NIM yang ditulis secara vertikal kebawah sebanyak len dari NIM lalu ditambah character html yang diinginkan dan sebuah separator tertentu
  
  Dari kode diatas dengan, modifikasi kode yang diberikan dengan s += char diperoleh output yang error karena code 'char' tidak terdefinisi. Untuk modifikasi kode yang diberikan dengan s += char1 diperoleh output NIM sesuai urutan secara horizontal dan setiap angka NIM diwakilkan dengan kotak berwarna putih sesuai dengan jumlah angkanya. Untuk modifikasi kode yang diberikan dengan s += char2 diperoleh output NIM sesuai urutan secara horizontal dan setiap angka NIM diwakilkan dengan kotak berwarna hitam sesuai dengan jumlah angkanya.
