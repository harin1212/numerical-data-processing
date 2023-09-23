import numpy as np
import matplotlib.pyplot as plt

#뷔퐁의 바늘문제
#랜덤값 분포에 맞게 잡으면 시뮬레이션이랑 똑같음

n = 15000
num = 0
for i in range(1,n+1): #시뮬레이션 횟수
    u = 1/2 * np.random.rand()
    v = np.pi * np.random.rand() #세타
    if u <= 1/2 * np.sin(v):
        num = num + 1
if i % 1000 == 0: #1000단위로 확률 나타내기
        #i : 전체 영역의 점 개수, num : 영역 안의 점 개수
        # num/i = 2/pi ~> 2*i/num = pi
        print([i,2*i/num, np.pi]) #pi값 보이기 