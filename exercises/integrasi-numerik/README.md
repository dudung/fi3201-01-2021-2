# Integrasi Numerik

## Table of Contents

- [About](#about)
- [Note](#note)
- [Problem](#problem)


## About <a name = "about"></a>

Materials:
- Integrasi Numerik
    - [`Aturan persegi panjang titik awal`](0301-rectangle-beg-point.py)
    - [`Aturan persegi panjang titik akhir`](0301-rectangle-end-point.py)
    - [`Aturan persegi panjang titik tengah`](0301-rectangle-mid-point.py)
    - [`Aturan trapesium`](0301-trapezoidal.py)
    - [`Aturan simpson`](0301-simpson.py)

Material for 6.2th of weeks.

## Note <a name = "note"></a>

Akses kode program via link di <a name="about">`About`</a>.

1. **Aturan persegi panjang titik awal**

    <img width="45%" src="https://www.mathsisfun.com/calculus/images/integral-approx-1.gif">\
    Output:
    ```python
    Rectangle Rule Beg Point
    f(x) =  3x^2
    xbeg =  1
    xend =  2
    N =  10
    integral =  6.555000000000004

    N =  1000
    integral =  6.995500499999447

    N =  1000000
    integral =  6.999995499589404
    ```

2. **Aturan persegi panjang titik akhir**

    <img width="45%" src="https://www.mathsisfun.com/calculus/images/integral-approx-2.gif">\
    Output:
    ```python
    Rectangle Rule End Point
    f(x) =  3x^2
    xbeg =  1
    xend =  2
    N =  10
    integral =  7.455000000000006

    N =  1000
    integral =  7.004500499999446

    N =  1000000
    integral =  7.0000044995894015
    ```


3. **Aturan persegi panjang titik tengah**

    <img width="45%" src="https://www.mathsisfun.com/calculus/images/integral-approx-3.gif">\
    Output:
    ```python
    Rectangle Rule Mid Point
    f(x) =  3x^2
    xbeg =  1
    xend =  2
    N =  10
    integral =  6.997500000000006

    N =  1000
    integral =  6.999999749999449

    N =  1000000
    integral =  6.999999999588539
    ```

4. **Aturan trapesium**

    <img width="45%" src="https://www.mathsisfun.com/calculus/images/integral-approx-4.gif">\
    Output:
    ```python
    Trapezoidal rule
    f(x) =  3x^2
    xbeg =  1
    xend =  2
    N =  10
    integral =  7.005000000000004

    N =  2
    integral =  7.125

    N =  1000
    integral =  7.000000499999455

    N =  1000000
    integral =  6.999999999589312
    ```

5. **Aturan simpson**

    <img width="45%" src="https://www.mathsisfun.com/calculus/images/integral-approx-5.gif">\
    Output:
    ```python
    Simpson rule
    f(x) =  3x^2
    xbeg =  1
    xend =  2
    N =  10
    integral =  7.0

    N =  2
    integral =  7.0

    N =  1000
    integral =  7.000000000000009

    N =  1000000
    integral =  7.0000000001438645
    ```
    
    > Simpson ini paling bagus

## Problem <a name = "problem"></a>