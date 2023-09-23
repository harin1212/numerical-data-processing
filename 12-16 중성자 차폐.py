import numpy as np

n = 5000
num = 0

for i in range(1,n+1): #시뮬레이션 횟수
    x = 1 #오른쪽으로 간 거리
    for j in range(1,8): #7번
        v = np.pi*np.random.rand() #0<theta<pi
        x = x + np.cos(v)
        if x > 5 :
            num = num + 1
            break
    if i % 1000 == 0 :
        print([i,num/i*100])