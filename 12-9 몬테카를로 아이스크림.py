import numpy as np

#원 안에 n개의 점 찍기
n = 5000
num_A = 0 #전체 점의 개수
num_D = 0 #영역 안에 점

while num_A < n:
    x = 2*np.random.rand() -1
    y = 2*np.random.rand() -1
    z = 2*np.random.rand() 
    num_A = num_A + 1 #박스 안의 점의 개수 카운트
    if np.sqrt(x**2 + y**2) <=z and x**2 + y**2 + (z-1)**2 <=1:
        num_D = num_D + 1 #조건 만족시 영역 안의 점개수 카운트
    if num_A % 1000 == 0 :
        print([num_A,num_D,8*num_D/num_A]) #박스의 부피 8 곱해줌
    