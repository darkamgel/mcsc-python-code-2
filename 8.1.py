import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def f(x, y):
    return x**2+x
x0 = 0
y0 = 1
intervals = np.linspace(0, 2, 21)
h = intervals[1] - intervals[0]
y = list()
y.append(y0)
for x in intervals[1:]:
    x0 = x
    yi = y[-1] + h*f(x0, y[-1])
    y.append(yi)
df = pd.DataFrame()
df["xi"]= intervals
df["yi"] = y
print(df)
plt.plot(intervals, y)
plt.title("Euler method plot of differential equation dy/dx=x^2+x")
plt.show()
