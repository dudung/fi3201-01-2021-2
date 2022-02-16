# 0480-matrix-no-numpy-sub.py
# Substract two matrices
# 20220216 Create this example.

import matrix as mat

# substract two two-dimension matrices in form of a list
def submat(m1, m2):
    # assume both matrices have the same dimension
    row = len(m1)
    col = len(m1[0])

    # create empty matrix
    m3 = []

    # iterate through rows then colums
    for r in range(row):
        newrow = []
        for c in range(col):
            newcol = m1[r][c] - m2[r][c]
            newrow.append(newcol)
        m3.append(newrow)
    
    return m3


# define a list as two-dimension matrix
m1 = [
    [1, 2, 3],
    [4, 5, 6]
    ]

m2 = [
    [1, -2, -3],
    [1, -4, 3]
    ]

m3 = submat(m1, m2)


# display results
print("m1:")
mat.printmat(m1)
print("m2:")
mat.printmat(m2)
print("m3 = m1 - m2:")
mat.printmat(m3)