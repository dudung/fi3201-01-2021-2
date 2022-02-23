# 0301-trapezoidal.py
# Integration with trapezoidal rule
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

# define number of trapezoidal areas
N = 10
dx = (xend - xbeg) / N

# calculate definite integral
total = 0
x = xbeg
for i in range(N):
  area = (f(x) + f(x+dx)) * dx / 2
  total = total + area
  x = x + dx

# display results
print("Trapezoidal rule")
print("f(x) = ", fxs)
print("xbeg = ", xbeg)
print("xend = ", xend)
print("N = ", N)
print("integral = ", total)
