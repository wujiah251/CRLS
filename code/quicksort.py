import random

def quicksort(A,start,end):
    if start>=end:
        return
    q=partition(A,start,end)
    quicksort(A,start,q-1)
    quicksort(A,q+1,end)
    
    
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



A=[2,8,7,1,3,5,6,4]
quicksort(A,0,7)
print(A)