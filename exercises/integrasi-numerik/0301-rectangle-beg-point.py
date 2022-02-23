# 0301-rectangle-beg-point.py
# Integration with rectangle rule beg point
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

# define number of rectangle areas
N = 10
dx = (xend - xbeg) / N

# calculate definite integral
total = 0
x = xbeg
for i in range(N):
  area = f(x) * dx
  total = total + area
  x = x + dx

# display results
print("Rectangle Rule Beg Point")
print("f(x) = ", fxs)
print("xbeg = ", xbeg)
print("xend = ", xend)
print("N = ", N)
print("integral = ", total)
