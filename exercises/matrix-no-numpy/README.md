# matrix-no-numpy

## Table of Contents

- [About](#about)
- [Note](#note)
- [Problem](#problem)


## About <a name = "about"></a>

Some operator of matrix without numpy. Contents of lecture are:
- printmat
- addmat
- submat
- mulmat1, mulmat2
- empty matrix
- create library



## Note <a name = "note"></a>

- Hati-hati perintah penugasan di Python tidak sama C++. Di Python, sifatnya variabel reference
    ```python
    # misal ada matrix m1
    m1 = [
        [1,2,3],
        [4,5,6]
    ]
    # mau buat matrix m2 yg ukurannya sama
    m2 = m1
    m2[0][0] = 100
    
    print(m1)
    print()
    print(m2)
    ```

    Outputnya akan `m1 = m2`. Padahal yg diubah adalah `m2[0][0]`. Hati^2 !!

## Problem <a name = "problem"></a>

Akan ada asignment 4 di github. Pantau!