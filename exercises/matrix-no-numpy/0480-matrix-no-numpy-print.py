# 0480-matrix-no-numpy-print.py
# Define and view a matrix
# 20220216 Create this example.

# print only two-dimension matrix in form of a list
def printmat(m):
    # assume that all rows have the same number of columns
    row = len(m)
    col = len(m[0])

    # iterate through rows then colums
    for r in range(row):
        for c in range(col):
            print(m[r][c], end='\t')
        print()


# define a list as two-dimension matrix
m = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [9, 8, 0, 4, 2]
    ]

# display result
print("Print a matrix directly:")
print(m)

print()

print("Print a matrix using printmat() function:")
printmat(m)

print("Print row r:")
print(m[0]) # r=0

print("Print column c:")
for i in range(len(m)):
    print(m[i][0])
