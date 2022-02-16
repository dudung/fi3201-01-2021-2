# 0480-matrix-no-numpy-empty.py
# Create an empty matrix with dimensions row and col
# 20220216 Create this example.

import matrix as mat

# create an new two-dimension matrix in form of a list filled with zero
def newmat(row, col, val):
    # create empty matrix
    m = []

    # iterate through rows then colums
    for r in range(row):
        newrow = []
        for c in range(col):
            newrow.append(val)
        m.append(newrow)
    
    return m

# create a new zero matrix
row = 3
col = 4
val = 0
m = newmat(row, col, val)

# display results
print("row:")
print(row)
print("col:")
print(col)
print("m:")
mat.printmat(m)