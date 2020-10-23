import numpy as np
import math
from prettytable import PrettyTable
np.set_printoptions(precision=5)
def exp_predict(x_pred):
 # Data:
 x = np.array([2, 4, 6, 8, 10])
 y = np.array([4.077, 11.084, 30.128, 81.897, 222.62])
 # Equation Variables:
 a1 = len(x)
 b1 = x.sum()
 c1 = sum(np.log(y))
 a2 = x.sum()
 b2 = sum(x**2)
 c2 = sum(x*np.log(y))
 # Matrix Representation of equations:
 A = np.array([[a1, b1],
 [a2, b2]])

 b = np.array([c1, c2])
 # Solve Equations:
 a0, a1 = np.linalg.solve(A, b)
 # Predict:
 return np.exp(a0) * np.exp(a1 * x_pred)
print(exp_predict(9))