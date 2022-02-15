# 0452-qp-ls-lr-poly3.pg
# Impelement QP for LS in the case of LR for POLY3
# Sparisoma Viridi | https://github.com/dudung/bug
# 20220215 Create this program.

# abbreviations
# QP quaratic programming
# LS least square
# LR linear regression
# POLY3 polynomial function of 3rd order

# import numpy
import os, sys
import numpy as np

# open file, read lines and store them in a list, close file
fn = '0452-a.txt'
print('file:', fn)
with open(os.path.join(sys.path[0], fn), 'r') as f:
    lines = f.readlines()

# create empty list
x = [[]]
y = [[]]
A = []

# iterate through lines but ommit the first element
for l in lines[1:]:
    s = l.rstrip('\n') 
    s = s.split('\t')
    xi = float(s[0])
    yi = float(s[1])

    x[0].append(xi)
    y[0].append(yi)
    
    p0 = 1
    p1 = xi
    p2 = xi**2
    p3 = xi**3
    Ai = [p0, p1, p2, p3]
    A.append(Ai)

# create numpy array
x = np.transpose(np.array(x))
y = np.transpose(np.array(y))
A = np.array(A)

# find c via some temporary variables
AT = np.transpose(A)
ATA = np.matmul(AT, A)
ATA_1 = np.linalg.inv(ATA)
ATA_1AT = np.matmul(ATA_1, AT)
c = np.matmul(ATA_1AT, y)

# print dimension of matrices
print()
print('y:', y.shape)
print('A:', A.shape)
print('AT:', AT.shape)
print('ATA:', ATA.shape)
print('ATA_1:', ATA_1.shape)
print('ATA_1AT:', ATA_1AT.shape)
print('c: ', c.shape)

# print results
print()
print('c = ')
print(c)