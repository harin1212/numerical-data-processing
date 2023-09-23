import numpy as np
import matplotlib.pyplot as plt

#사각형 안에 5000개의 점 찍기
n = 5000
X = np.zeros(n)
Y = np.zeros(n)
j=0 #카운트

#사각형 안의 점 찍기
while j < n:
    x = 2*np.random.rand() - 1 #(-1,1)
    y = 2*np.random.rand() - 1 #(-1,1)
    
    if (abs(x) + abs(y)) <= 1:
        X[j], Y[j] = x, y
    j = j + 1

##|x|+|y|<=1
Xk = [-1,0,1]
Yk1 = [0,1,0]
Yk2 = [0,-1,0]
plt.plot(Xk,Yk1,'b-')
plt.plot(Xk,Yk2,'b-')
plt.plot(X,Y,'.')
plt.show()