# matrix.py
# Simple matrix library using list
# 20220216 Create this example.

# print only two-dimension matrix in form of a list
def printmat(m):
    # assume that all rows have the same columns
    row = len(m)
    col = len(m[0])

    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            print(m[r][c], end='\t')
        print()
    print()

# create an new two-dimension matrix in form of a list filled with zero
def newmat(row, col):
    # create empty matrix
    m = []

    # iterate through rows then colums
    for r in range(row):
        newrow = []
        for c in range(col):
            newrow.append(0)
        m.append(newrow)
    
    return m

# add two two-dimension matrices in form of a list
def addmat(m1, m2):
    # assume both matrices have the same dimension
    row = len(m1)
    col = len(m1[0])

    # create empty matrix
    m3 = []

    # iterate through rows then colums
    for r in range(row):
        newrow = []
        for c in range(col):
            newcol = m1[r][c] + m2[r][c]
            newrow.append(newcol)
        m3.append(newrow)
    
    return m3
    
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

# create an new two-dimension matrix in form of a list filled with zero
def newmat(row, col):
    # create empty matrix
    m = []

    # iterate through rows then colums
    for r in range(row):
        newrow = []
        for c in range(col):
            newrow.append(0)
        m.append(newrow)
    
    return m

# multiply a matrix with a scalar
def mulmat1(m, a):
    # assume all rows have the same number of columns
    row = len(m)
    col = len(m[0])

    m2 = newmat(row, col)
    
    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            m2[r][c] = m[r][c] * a

    return m2

# multiply a matrix with a matrix
def mulmat2(m1, m2):
    # assume colum of 1st and row of 2nd are matched
    row = len(m1)
    mid = len(m1[0])
    col = len(m2[0])

    m3 = newmat(row, col)
    
    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            temp = 0
            for m in range(mid):
                temp = temp + m1[r][m] * m2[m][c]
            m3[r][c] = temp

    return m3
