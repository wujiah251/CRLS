'''
基于随机划分的选择算法
'''
import random

def partition(A,start,end):
    key = A[end]
    i = start - 1
    for j in range(start,end):
        if A[j]<=key:
            i+=1
            tmp=A[i]
            A[i]=A[j]
            A[j]=tmp
    tmp=A[i+1]
    A[i+1]=A[end]
    A[end]=tmp
    return i+1

def randomized_partition(A,start,end):
    k=random.randint(start,end)
    tmp=A[k]
    A[k]=A[end]
    A[end]=tmp
    return partition(A,start,end)

def randomized_select(A,start,end,i):
    if start==end:
        return A[start]
    q = randomized_partition(A,start,end)
    k = q-start+1
    if i==k:
        return A[k]
    elif i<k:
        return randomized_select(A,start,q-1,i)
    else:
        return randomized_select(A,q+1,end,i-k)


A=[random.randint(1,30) for i in range(30)]
x=randomized_select(A,0,29,10)
print(x,A)