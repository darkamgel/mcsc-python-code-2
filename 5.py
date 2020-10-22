x = [0,1,3,4,5]
y = [0,1,81,256,625]
# Reading interpolation point
xp = 2
# Set interpolated value initially to zero
yp = 0
# Implementing Lagrange Interpolation
for i in range(5):
    p = 1
    for j in range(5):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]
# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))    
