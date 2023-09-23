import numpy as np
import matplotlib.pyplot as plt

n, a, b, x, y = 100, 0, 1, 1, 0
t = a
h = (b-a)/n
T = [t]
X = [x]
Y = [y]
for k in range(1,n+1):
    x1 = x - y + t*(2-t*(1+t))
    y1 = x + y + t**2*(-4+t)
    x2 = x1 - y1 + 2 - t*(2+3*t)
    y2 = x1 + y1 + t*(-8+3*t)
    x3 = x2 - y2 - 2 - 6*t
    y3 = x2 + y2 - 8 + 6*t
    x4 = x3 - y3 -6
y4 = x3 + y3 +6
x = x + h*x1 + 1/2*h**2*x2 + 1/6*h**3*x3 + 1/24*h**4*x4
y = y + h*y1 + 1/2*h**2*y2 + 1/6*h**3*y3 + 1/24*h**4*y4
t = t + h
T.append(t)
X.append(x)
Y.append(y)

print('%4s %9s %9s %9s' % ('n', 't', 'x', 'y'))
for i in range(0, n + 1):
    print('%4d %9.4f %9.8f %9.8f' % (i, T[i], X[i], Y[i]))

plt.plot(T,X,'*')
plt.plot(T,Y,'-')
plt.show()