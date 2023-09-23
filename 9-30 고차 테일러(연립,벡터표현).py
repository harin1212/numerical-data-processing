import numpy as np
import matplotlib.pyplot as plt

n, a, b, x, y = 100, 0, 1, 1, 0
t = a
h = (b-a)/n
T,X,Y = [t], [x], [y]
d = np.array([x,y])

for k in range(1,n+1):
    d1 = np.array([d[0] - d[1] + t*(2-t*(1+t)), d[0] + d[1] + t**2*(-4+t)])
    d2 = np.array([d1[0] - d1[1] + 2 - t*(2+3*t), d1[0] + d1[1] + t*(-8+3*t)])
    d3 = np.array([d2[0] - d2[1] - 2 - 6*t, d2[0] + d2[1] - 8 + 6*t])
    d4 = np.array([d3[0] - d3[1] -6, d3[0] + d3[1] +6])
    d = d + h*d1 + 1/2*h**2*d2 + 1/6*h**3*d3 + 1/24*h**4*d4
    t = t + h
    T.append(t)
    X.append(d[0])
    Y.append(d[1])

print('%4s %9s %9s %9s' % ('n', 't', 'x', 'y'))
for i in range(0, n + 1):
    print('%4d %9.4f %9.8f %9.8f' % (i, T[i], X[i], Y[i]))

plt.plot(T,X,'*')
plt.plot(T,Y,'-')
plt.show()