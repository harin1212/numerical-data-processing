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

def F(t,X): return np.array([0.6*X[0]*(1-X[0]/1000)-0.02*X[0]*X[1],-0.4*X[1]+0.001*X[0]*X[1]])
n = 100
a,b = 0,50 # 여우가 10, 32, 60일때 비교
h = (b-a)/n
t = a
T, X10, Y10 = RK4(F,t,[500,28],h,n)
T, X32, Y32 = RK4(F,t,[500,32],h,n)
T, X60, Y60 = RK4(F,t,[500,29],h,n)

'''
print('%4s %9s %9s %9s' %('n', 't', 'x', 'y'))
for i in range(0,n+1):
    print('%4d %9.4f %9.8f %9.8f' %(i,T[i],X[i],10*Y[i]))
'''
# plt.plot(T,X,'r-')
plt.plot(X10,Y10,'b-')
plt.plot(X32,Y32,'r-')
plt.plot(X60,Y60,'g-')
plt.show()