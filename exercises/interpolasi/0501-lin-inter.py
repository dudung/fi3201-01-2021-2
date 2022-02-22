# 0501-lin-inter.py
# Linear interpolation
# Sparisoma Viridi | https://github.com/dudung
# 20220221 Create this example.

# import package
import numpy as np

# define data points
x = [1, 4, 7, 10]
y = [11, 18, 7, 5]

# create coefficients c0 and c1 with zero values
c0 = [0, 0, 0]
c1 = [0, 0, 0]

# calculate c0 and c1
N = len(c0)
for i in range(N):
  c1[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
  c0[i] = y[i] - c1[i] * x[i]

# define linear interpolation function f(x)
def f(xx):
    i = int(np.floor((xx - x[0])/(x[1] - x[0])))
    if i > N - 1:
        i = i - 1
    y = c0[i] + c1[i] * xx
    return y

# use the function
for xx in range(1, 11):
  yy = f(xx)
  print(xx, yy)
