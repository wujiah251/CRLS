import random
from time import time

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
   
def randomized_quicksort(A,start,end):
    if start>=end:
        return
    q=randomized_partition(A,start,end)
    quicksort(A,start,q-1)
    quicksort(A,q+1,end)

def randomized_partition(A,start,end):
    k=random.randint(start,end)
    tmp=A[k]
    A[k]=A[end]
    A[end]=tmp
    return partition(A,start,end)

def hoare_quicksort(A,start,end):
    if start>=end:
        return
    q=partition(A,start,end)
    quicksort(A,start,q-1)
    quicksort(A,q+1,end)

def hoare_partition(A,start,end):
    i=start
    j=end
    key=A[start]
    while True:
        while A[j]>=key and i<j:
            j-=1
        if i==j:
            A[i]=key
            return i
        else:
            A[i]=A[j]
            i+=1
        while A[i]<=key and i<j:
            i+=1
        if i==j:
            A[i]=key
            return i
        else:
            A[j]=A[i]
            j-=1


def tail_recursive_quicksort(A,start,end):
    stack=[]
    stack.append((start,end))
    while stack:
        s,e=stack.pop()
        if s>=e:
            continue
        q=partition(A,s,e)
        stack.append((s,q-1))
        stack.append((q+1,e))

A=[2,8,7,1,3,5,6,4]
tail_recursive_quicksort(A,0,7)
print(A)

