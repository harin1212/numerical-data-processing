import numpy as np

num=51
for n in range(1,num):
    p = 1
    for k in range(1,n+1):
        p = p * (365-k+1)/365

        
# 시뮬레이션
res = 0
for k in range(0,1000):
    #n칸 배열
    B = np.zeros(n)
    for j in range(0,n):
        B[j] = int(np.ceil(365*np.random.rand()))
    if len(set(B)) < n: #집합은 중복 요소 하나로 체크 -> 집합 길이<n이면 같은 생일 있는것
        res = res + 1
        
if n % 5 == 0:
    print([n,round((1-p)*100)/100, res/1000])
