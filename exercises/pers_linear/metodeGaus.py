"""
    Program for making invers of matrix using Gauss elimination

    Translated to .py format from metodeGauss.cpp
"""

from tkinter import N


def display(x, N):
    M = N + 1   # column
    for i in range(N):
        for j in range(M):
            k = M*i + j
            print( "{:.1f}".format(x[k]), end="")
            #print(x[k], end="")
            if(j < M-1): print("\t", end="")
        print()

def main():
    N = 4   # row

    # array 2D in array 1D
    r = [
        1, 1, 1, 1, 10,
        4, 1, 3, 1, 19, 
        2, 1, 1, 1, 11,
        1, 3, 1, 2, 18,
    ]
    """
    r = {
        1, 3, 4, 1, 12,
        0, 12, 0, 2, 4,
        0, 0, 2, 1, 1,
        0, 0, 0, 1, -1,
    }
    """

    # display initial matrix
    print("Initial matrix")
    display(r, N)

    # index array start from 0
    for k in range(N-1):
        for i in range((k+1), N):
            ik = (N+1)*i + k
            cik = r[ik]
            for j in range(k, N+1):
                ij = (N+1)*i + j
                kj = (N+1)*k + j
                kk = (N+1)*k + k
                r[ij] = r[ij] - cik*r[kj]/r[kk]
    
    print()
    print("Matrix of row echelon")
    display(r, N)

    x = [None] * N
    
    for i in range((N-1), -1, -1):  #stop di 0
        c = 0
        for j in range((N-1), i, -1):
            ij = (N+1)*i + j
            c = c + x[j]*r[ij]
        iM = (N+1)*i + N
        ii = (N+1)*i + i
        x[i] = (r[iM] - c)/r[ii]
    
    print()
    print("Solution")

    for i in range(N):
        print( "{:.1f}".format(x[i]) )
        #print(x[i])

main()  #call main function