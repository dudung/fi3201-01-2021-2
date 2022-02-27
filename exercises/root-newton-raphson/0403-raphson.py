# 0403-newton-raphson.py
# Impelement Newton-Raphson method
# Sparisoma Viridi | https://github.com/dudung/bug
# 20220126 Create this program.

# define a polynomial function and its derivativve
def poly(x):
    x1 = 2.0
    x2 = 5.0
    x3 = 9.87654321
    f = (x - x1) * (x - x2) * (x - x3)
    fx1 = (x - x2) * (x - x3)
    fx2 = (x - x1) * (x - x3)
    fx3 = (x - x1) * (x - x2)
    fx = fx1 + fx2 + fx3
    return f, fx

# define initial conditions
x1 = 100

# define accuracy
eps = 1E-14

# Set initial error
f1, fx1 = poly(x1)
err = abs(f1)

# Find a root
n = 0
print("n x")
while err > eps:
    f1, fx1 = poly(x1)
    x2 = x1 - f1 / fx1
    f2, fx2 = poly(x2)
    err = abs(f1)
    x1 = x2
    n = n + 1
    print(n, x2)

# Resume result
print("step = ", n, sep='')
print("err = ", err, sep='')
print("root = ", x1, sep='')