import numpy as np 
#u1,u2,u3
#q1=u1/|u1|
#q2=v2/|v2|, v2=u2-(u2●q1)q1
#q3=v3/|v3|, v3=u3-(u3●q1)q1+(u3●q2)q2

#행렬 A의 행을 직교화 한다.
#u1={1,1,1}, u2={0,1,1}, u3={0,0,1}

def GramS(A) :
    n = len(A)
    #Q의 행들이 q1,q2,..
    Q = np.zeros((n,n)) 
    Q[0,:] = A[0,:]/(np.sqrt(np.dot(A[0,:],A[0,:])))

    for i in range(1,n) :
        temp = 0
        for j in range(0,i) :
            temp = temp + np.dot(A[i,:],Q[j,:]) * Q[j,:]
        Q[i,:] = A[i,:]-temp
        Q[i,:] = Q[i,:]/(np.sqrt(np.dot(Q[i,:],Q[i,:])))

    return Q

A=np.array([[1,1,1],[0,1,1],[0,0,1]])
Q = GramS(A)
print(Q)