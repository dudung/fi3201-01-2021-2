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
    s += char2 
  print(n, ':', s, sep='') 
  ```
  ## Answer 1
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
  ![alt text](https://github.com/AkramAkbarAmin/fi3201-01-2021-2/blob/main/assignments/03/10218009_Assignment%203_Answer%20for%20question%201.png)
