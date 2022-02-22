# 0502-lagrange-inter.py
# Lagrange interpolatio
# Sparisoma Viridi | https://github.com/dudung
# 20220222 Create this example.

# define data points
x = [1, 4, 7, 10]
y = [11, 18, 7, 5]
N = min(len(x), len(y))


# define lagrange interpolating polynomial function p(x)
def prod(i, xx):
  prod = 1
  for j in range(N):
    if j != i:
      prodj = (xx - x[j]) / (x[i] - x[j])
    else:
      prodj = 1
    prod = prod * prodj

  return prod

def p(xx):
  sum = 0
  for i in range(N):
    pi = y[i] * prod(i, xx)
    sum = sum + pi
  
  return sum

# use the function
for xx in range(1, 11):
  yy = p(xx)
  print(xx, "%.3f" % yy)