import numpy as np
# Reading number of unknowns
n = int(input('Enter number of data points: '))
# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n,n))
# x = np.array([0.20, 0.22, 0.24, 0.26, 0.28, 0.30])
# y = np.append([[1.6596],[1.6698], [1.6804], [1.6912], [1.7024], [1.7139]])
# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
# Generating forward difference table
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]
print('\nFORWARD DIFFERENCE TABLE\n')
for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.2f' %(y[i][j]), end='')
    print()
# Generating backward difference table
for i in range(1, 6):
    for j in range(6-1,i-2,-1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

print('\nBACKWARD DIFFERENCE TABLE\n')
for i in range(0,6):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, i+1):
        print('\t%0.2f' %(y[i][j]), end='')
    print()