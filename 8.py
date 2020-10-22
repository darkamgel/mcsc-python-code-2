# Euler method python program

# function to be solved
def f(x, y):
    return x + y


# Euler method
def euler(x0, y0, xn, n):
    # Calculating step size
    h = (xn - x0) / n

    print('\n-----------SOLUTION-----------')
    print('------------------------------')
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, slope, yn))
        print('------------------------------')
        y0 = yn
        x0 = x0 + h
    print('\nAt x=%.4f, y=%.4f' % (xn, yn))


# Inputs
print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
xn = float(input('xn = '))

print('Enter number of steps:')
step = int(input('Number of steps = '))

# Euler method call
euler(x0, y0, xn, step)