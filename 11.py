import numpy as np
import math
from prettytable import PrettyTable
np.set_printoptions(precision=5)
def linear_predict(x_pred):
 # Data:
    x = np.array([1, 2, 3, 4, 5, 6])
    y = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])
 # Equation Variables:
    a1 = len(x)
    b1 = x.sum()
    c1 = y.sum()
    a2 = x.sum()
    b2 = sum(x**2)
    c2 = sum(x*y)
 # Matrix Representation of equations:
    A = np.array([[a1, b1],
    [a2, b2]])
    b = np.array([c1, c2])
 # Solve Equations:
    a0, a1 = np.linalg.solve(A, b)
 # Predict:
    return a0 + (a1 * x_pred)
print(linear_predict(x_pred=2.5))