import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#푸리에 급수
#p : 주기의 반=pi
def Fouriercoeff(f,N,p):
    A = np.zeros(N+1) #a0도 생각
    B = np.zeros(N+1) #b0=0
    A[0] = 1/p * quad(f,-p,p)[0] #quad:적분, quad()[0]: 적분값
    for i in range(1,N+1) :        
        g = lambda x : f(x) * np.cos(i*np.pi*x)
        A[i] = 1/p * quad(g,-p,p)[0]
        h = lambda x : f(x) * np.sin(i*np.pi*x)
        B[i] = 1/p * quad(h,-p,p)[0]
    return A,B

# 한 주기만큼 함수 정의하기
def f(x):
    if x>-1 and x<=0:
        return x+1
    elif x>0 and x<1 :
        return 1

# 주기 만들어줌
#floor : 가우스 함수(내림)
def g(x):
    return f(x-2*np.floor((x+1)/(2))) #x-2pi [(x+pi)/2*pi]

#print(Fouriercoeff(g,4,1)) #N=4

#sinx+cosx
def p(x,N):
    A,B = Fouriercoeff(g,N,np.pi)
    n = len(A)
    res = 1/2 * A[0]
    for i in range(1,n):
        res = res + A[i] * np.cos(i*np.pi*x) + B[i] * np.sin(i*np.pi*x)
    return res

Xk = np.arange(-10,10,0.1)
Yk = [g(xk) for xk in Xk]
Zk1 = [p(xk,1) for xk in Xk] # N=1
Zk2 = [p(xk,2) for xk in Xk] # N=2
Zk3 = [p(xk,3) for xk in Xk] # N=3
Zk4 = [p(xk,4) for xk in Xk] # N=4

plt.plot(Xk,Yk,'.')
plt.plot(Xk,Zk1,'-')
plt.plot(Xk,Zk2,'-')
plt.plot(Xk,Zk3,'-')
plt.plot(Xk,Zk4,'-')
plt.show()