# QUADRATIC PROGRAMMING

## Table of Contents

- [About](#about)
- [Answer](#answer)
- [Problem](#problem)


## About <a name = "about"></a>

Contents of lecture are:
- Formula
- Least square
    - Linear regression

It can be accessed at [here](https://bugx.vercel.app/pages/0452.html).


## Answer <a name = "answer"></a>

> **Soal 1**
1. Question

    Answer


## Problem <a name = "problem"></a>

Akan dilakukan optimasi suatu fungsi obyektif kuadratik yang tunduk pada kendala linear.

Ada data mentah [0452-a.txt](0452-a.txt).

Dengan menggunakan excel, diperoleh \
<img src="1.jpg" width="65%">

Dengan Python:\
Manfaatkan [Pers.12](https://bugx.vercel.app/pages/0452.html#:~:text=dengan%20nol%20untuk-,meminimumkannya,-%E2%88%82).

Program ada di [sini](0452-qp-ls-lr-poly3.py).

Output:
```
y: (101, 1)
A: (101, 4)
AT: (4, 101)
ATA: (4, 4)
ATA_1: (4, 4)
ATA_1AT: (4, 101)
c:  (4, 1)

c =
[[ 0.75618375]
 [ 3.35558613]
 [-0.36394393]
ATA: (4, 4)
ATA_1: (4, 4)ATA_1AT: (4, 101)c:  (4, 1)

c =
[[ 0.75618375]
 [ 3.35558613]
 [-0.36394393]
 [ 0.01210265]]
```
Compiled in local.