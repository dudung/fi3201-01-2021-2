# 0402-bisection-with-list.py
# Calculate root using bisection method
# Sparisoma Viridi | https://github.com/dudung/bug
# 20220126 Create this program.

# define a quadratic function
def f(x):
    a = 1
    b = -20
    c = 45
    y = a*x*x + b*x + c
    return y

# define initial value using list
x = [0.0, 1.0]
i = len(x)

# define error and accuracy
err = abs(f(x[i-1]))
eps = 1E-2

# peform calculation
while err > eps:
    xnew = 0.5 * (x[i-1] + x[i-2])
    x.append(xnew)

    err = abs(f(x[i-1]))
    
    if f(x[i]) * f(x[i-1]) > 0:
        x[i-1], x[i-2] = x[i-2], x[i-1]

    # display results
    if i == 2:
        print("x = ")
        print(x[0])
        print(x[1])
    else:
        print(x[i])
    
    i = len(x)

# display error and accuracy
print("err = ", err, sep='')
print("eps = ", eps, sep='')
