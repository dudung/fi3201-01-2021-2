#Assignment 03
Digunakan kode sebagai berikut
```python
import html #Mengimport module html, hanya dapat dilakukan bila sudah menginstall html dengan pip install html
char1 = html.unescape('&#x25FB;') #unicode character untuk kotak berwarna putih beroutline hitam
char2 = html.unescape('&#x25FC;') #unicode character untuk kotak berwarna hitam beroutline hitam
NIM = '10218010' #dibaca sebagai string karena perintah berikutnya tidak memungkinkan sebagai iterasi dari integer
for x in NIM: #fungsi for yang didefinisikan untuk setiap x didalam variabel NIM
  n = int(x, 10) #transformasi integer dari setiap character NIM yang terhitung didalam x dan mengizinkan pembuatan kotak hingga 9
  s = '' #berguna untuk mendefinisikan apa yang ditampilkan dari setiap character dalam NIM
  for i in range(n): #definisi for yang baru
    s += char #s digunakan sebagai substitusi variabel baru berdasarkan kode html yang diberikan (+= berarti menjumlahkan variabel dan menjadikan nilai s bernilai sebesar hasil penjumlahan tersebut)
  print(n, ':', s, sep='') #hasilnya akan berupa setiap character NIM yang ditulis secara vertikal kebawah sebanyak len dari NIM lalu ditambah character html yang diinginkan dan sebuah separator tertentu, disini adalah spasi atau tidak sama sekali
```
#Jawaban 1
Hasil dari koding tersebut adalah
![alt text]()

#Jawaban 2
Hasil dari permintaan char1 adalah
![alt_text]()

#Jawaban 3
Hasil dari permintaan char2 adalah
![alt_text]()

#Jawaban 4
Kode diatas digunakan untuk
```
Menampilkan character html unicode tertentu yang jumlahnya sama dengan masing-masing karakter dari NIM yang ada
10218010 akan diwakilkan dengan kotak yang disusun kebawah, sehingga pada saat nilai hasil for menunjuk pada 1 maka akan muncul 1 kotak dan ketika 8 akan muncul 8 kotak
```
