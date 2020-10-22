import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 0
    else:
        return x**2-64*x+10
xi = np.arange(0,1.1,0.1)
h = 0.1
yi = list()
yi.append(0)
for i in xi[1:-1]:
    y = (f(i+h)-2*f(i)+f(i-h))/h**2
    yi.append(y)
yi.append(0)

df = pd.DataFrame()
df["xi"]= xi
df["yi"] = yi
print(df)

plt.plot(xi, yi)
plt.title('''Finite different method plot of 2nd order method plot of differential equation y"-64y'+10=0''')
plt.show()
