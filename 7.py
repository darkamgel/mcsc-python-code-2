import numpy as np
def f(x):
    return np.power(1/(2 * np.pi), 1/2) * np.exp(-x**2 / 2)
# Implementing Simpson's 1/3 
def simpson13(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    # Finding sum 
    integration = f(x0) + f(xn)
    for i in range(1,n):
        k = x0 + i*h
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    integration = integration * h/3
    return integration
lower_limit = -4
upper_limit = 4
sub_interval = 50
# Call simpson13() method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )