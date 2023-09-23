import numpy as np

#원 안에 5000개의 점 찍기
n = 5000
j=0 #카운트
sum=0

#중심 1/2,1/2 반지름 1/2인 원 -> 점 5000개
#랜덤넘버 : 0~1 사이
while j < n:
    x = np.random.rand() 
    y = np.random.rand() 
    
    if ((x-1/2)**2 + (y-1/2)**2) <= 1/4:
        sum = sum + np.sin(np.sqrt(np.log(x+y+1)))
        j = j + 1
        if j % 1000 == 0 :
            #적분값 영역의 넓이 
            res = np.pi/4 * sum / j
            print([j,res])