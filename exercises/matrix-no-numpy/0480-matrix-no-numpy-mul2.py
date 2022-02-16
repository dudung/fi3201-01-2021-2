# 0480-matrix-no-numpy-mul2.py
# Multiply a matrix with a matrix
# 20220216 Create this example.

import matrix as mat

# multiply a matrix with a matrix
def mulmat2(m1, m2):
    # assume column of 1st and row of 2nd are matched
    row = len(m1)       # m1 (row x mid)
    mid = len(m1[0])    # m2 (mid x col)
    col = len(m2[0])

    m3 = mat.newmat(row, col)
    
    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            temp = 0
            for m in range(mid):
                temp = temp + m1[r][m] * m2[m][c]
            m3[r][c] = temp

    return m3

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

m3 = mulmat2(m1, m2)

# display results
print("m1:")
mat.printmat(m1)
print("m2:")
mat.printmat(m2)
print("m3:")
mat.printmat(m3)
