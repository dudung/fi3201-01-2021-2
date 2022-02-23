# 0301-simpson.py
# Integration with simpson's rule
# Sparisoma Viridi | https://github.com/dudung
# 20220223 Start this example

# define a function
fxs = "3x^2"
def f(x):
  y = 3 * x * x
  return y

# define integral lower and upper bounds
xbeg = 1
xend = 2

# define number of half parabolic areas
N = 10
if (N / 2) != int(N /2):
	N = N + 1
dx = (xend - xbeg) / N
M = int(N / 2)

# calculate definite integral
total = 0
x = xbeg
for i in range(M):
  area = ( f(x) + 4 * f(x+dx) + f(x+2*dx) ) * dx / 3
  total = total + area
  x = x + 2 * dx

# display results
print("Simpson's rule")
print("f(x) = ", fxs)
print("xbeg = ", xbeg)
print("xend = ", xend)
print("N = ", N)
print("integral = ", total)
