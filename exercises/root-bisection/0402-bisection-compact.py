# 0402-bisection-compact.py
# Impelement bisection from only two equation
# Sparisoma Viridi | https://github.com/dudung/bug
# 20220126 Create this program.

# define a polynomial function
def poly(x):
    x1 = 2.0
    x2 = 5.0
    x3 = 9.0
    y = (x - x1) * (x - x2) * (x - x3)
    return y

# define initial conditions
x1 = 7.0
x2 = 10.0
x3 = 0.5 * (x1 + x2)

# define accuracy
eps = 1E-14

# Calculate initial error
err = abs(poly(x3))

# Find a root
n = 0
print("n x")
while err > eps:
    x4 = 0.5 * (x3 + x2) if poly(x3) * poly(x2) < 0 else 0.5 * (x3 + x1)
    err = abs(poly(x4))
    x1, x2, x3 = x2, x3, x4
    n = n +1
    print(n, x4)

# Resume result
print("step = ", n, sep='')
print("err = ", err, sep='')
print("root = ", x4, sep='')