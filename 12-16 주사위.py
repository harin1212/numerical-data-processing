import numpy as np
import matplotlib.pyplot as plt

#주사위 동시에 24번 던질 때 합이 12가 나올 확률
#숫자를 늘린다고 해서 정확도가 높아지는건 아니다
num = 0
n=5000
for i in range (1,n+1): #시뮬레이션 횟수
    for j in range (1,25): #주사위 던지는 횟수
        d1 = int(np.ceil(6*np.random.rand()))
        d2 = int(np.ceil(6*np.random.rand()))
        if d1 + d2 == 12 : 
            num = num + 1 
            break
    if i % 1000 ==0 : #1000단위로 확률 나타내기
        print([i,num/i])
print(num/5000)


#30보다 크면 i프린트 멈추기
'''
for i in range(1,101):
    if i<30:
        print(i)
    else : break
'''