import numpy as np

#원 안에 n개의 점 찍기
n = 5000
num_A = 0 #전체 점의 개수
num_D = 0 #영역 안에 점

while num_A < n:
    x = np.random.rand() 
    y = np.random.rand() 
    z = np.random.rand() 
    num_A = num_A + 1 #박스 안의 점의 개수 카운트
    if x**2 + np.sin(y) <= z and x-z+np.exp(y) <= 1:
        num_D = num_D + 1 #조건 만족시 영역 안의 점개수 카운트

    if num_A % 1000 == 0 :
        print([num_A,num_D, 1*num_D/num_A]) #영역부피=박스부피*영역점개수/박스안점 = 적분값
    