# 0480-matrix-no-numpy-mul1.py
# Multiply a matrix with a scalar
# 20220216 Create this example.

import matrix as mat

# multiply a matrix with a scalar
def mulmat1(m, a):
    # assume all rows have the same number of columns
    row = len(m)
    col = len(m[0])

    m2 = mat.newmat(row, col)
    
    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            m2[r][c] = m[r][c] * a

    return m2

# define a list as two-dimension matrix
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

a = 2
m2 = mulmat1(m1, a)


# display results
print("m1:")
mat.printmat(m1)
print("a:")
print(a)
print("m2 = m1 · a:")
mat.printmat(m2)