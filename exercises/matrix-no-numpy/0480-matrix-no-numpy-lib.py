# 0480-matrix-no-numpy-mul2.py
# Multiply a matrix with a matrix
# 20220216 Create this example.

import matrix as mat

# define a list as two-dimension matrix
m1 = [
    [1, 1, 1],
    [1, 2, 1],
    ]
m2 = [
    [1, 1],
    [1, 2],
    [1, 1],
    ]

m3 = mat.mulmat2(m1, m2)

# display results
print("m1:")
mat.printmat(m1)
print("m2:")
mat.printmat(m2)
print("m3:")
mat.printmat(m3)
