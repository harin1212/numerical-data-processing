import numpy as np
import matplotlib.pyplot as plt

def RK2(f,t,x,h,n):
    a = t
    T = [a]
    X = [x]
    for j in range(1,n+1):
        K_1 = h*f(t,x)
        K_2 = h*f(t+h,x+K_1)
        x = x + 1/2*(K_1 + K_2)
        t = a + j*h
        T.append(t)
        X.append(x)
    return np.array(T), np.array(X)

def f(t,x): return 1 + x**2 + t**3
n = 100
a,b,x = 1,2,-4
h = (b-a)/n
t = a
T, X = RK2(f,t,x,h,n)

print('%4s %9s %9s' %('n', 't', 'x'))
for i in range(0,n+1):
    print('%4d %9.4f %9.8f' %(i,T[i],X[i]))