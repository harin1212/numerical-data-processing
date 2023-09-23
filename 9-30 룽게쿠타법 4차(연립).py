import numpy as np
import matplotlib.pyplot as plt

def RK4(F,t,D,h,n):
    a = t
    T = [a]
    X, Y = [D[0]], [D[1]]  # D = [x,y]
for j in range(1,n+1):
    K_1 = h*F(t,D)
    K_2 = h*F(t+1/2*h,D+1/2*K_1)
    K_3 = h*F(t+1/2*h,D+1/2*K_2)
    K_4 = h*F(t+h,D+K_3)
    D = D + 1/6*(K_1+2*K_2+2*K_3+K_4)
    t = a + j*h
    T.append(t)
    X.append(D[0])
    Y.append(D[1])
    #return np.array(T), np.array(X), np.array(Y)

def F(t,X): return np.array([X[0]-X[1]+2*t-t**2-t**3,X[0]+X[1]-4*t**2+t**3])

n = 100
a,b,D = 0,1,[1,0]
h = (b-a)/n
t = a
T, X, Y = RK4(F,t,D,h,n)

print('%4s %9s %9s %9s' %('n', 't', 'x', 'y'))
for i in range(0,n+1):
    print('%4d %9.4f %9.4f %9.4f' %(i,T[i],X[i],Y[i]))

plt.plot(T,X,'-')
plt.plot(T,Y,'-')
plt.show()