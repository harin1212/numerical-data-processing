import numpy as np
import matplotlib.pyplot as plt

#원 안에 1000개의 점 찍기
n = 1000
X = np.zeros(n)
Y = np.zeros(n)
j=0 #카운트

#x와 y안 원 안의 점 찍기
while j < n:
    x = 4*np.random.rand() - 2 #(-2,2)
    y = 4*np.random.rand() - 2 #(-2,2)

    '''
    #x에 따라 y결정 -> 같은 y개수 다른 세로길이 => 양 끝에 점 몰림 (분포 몰림)
    X[j] = 4*np.random.rand() - 2
    Y[j] = (2* np.random.rand()-1)*(4-X[j]**2)**(1/2)
    '''

    '''
    #극좌표 x=rcospi seta, 0<=r<=2 / y=rsinpi seta, 0<=seta<=2
    #r과 seta 랜덤 -> 원의 중심으로부터 원의끝 점들의 개수 균등 => 원의 중심에 점 몰림(분포 몰림)
    r = np.random.rand()
    t = np.random.rand()
    X[j] = 2*r * np.cos(np.pi*2*t)
    Y[j] = 2*r * np.sin(np.pi*2*t)
    '''
    
    if (x**2 + y**2) <= 4:
        X[j], Y[j] = x, y
    j = j + 1

##반지름 2인 원 그리기 x**2+y**2=4
#0.01간격으로 x점 잡기
Xk = np.arange(-2,2,0.01)
Yk1 = (4-Xk**2)**(1/2)
Yk2 = -Yk1
plt.plot(Xk,Yk1,'b-')
plt.plot(Xk,Yk2,'b-')
plt.plot(X,Y,'.')
plt.show()