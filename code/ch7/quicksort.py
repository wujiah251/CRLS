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

# 非递归实现，栈实现
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


# 模糊排序
class interval:
    def __init__(self,left,right):
        self.left=left
        self.right=right

def fuzzy_partition(A,start,end):
    key=A[end]
    i=start
    j=start
    k=end
    while j<k:
        if A[j].right <= key.left:
            tmp=interval(A[i].left,A[i].right)
            A[i]=interval(A[j].left,A[j].right)
            A[j]=interval(tmp.left,tmp.right)
            i+=1
            j+=1
        elif A[j].left >= key.right:
            tmp=interval(A[k].left,A[k].right)
            A[k]=interval(A[j].left,A[j].right)
            A[j]=interval(tmp.left,tmp.right)
            k-=1
        else:
            key.left=A[j].left if A[j].left > key.left else key.left
            key.right=A[j].right if A[j].left < key.right else key.right
            j+=1
    return (i,k)

def fuzzy_quicksort(A,start,end):
    if start>=end:
        return
    a,b=fuzzy_partition(A,start,end)
    fuzzy_quicksort(A,start,a-1)
    fuzzy_quicksort(A,b+1,end)

A=[(2,4),(8,10),(7,11),(1,2),(3,7),(5,6),(6,9),(4,7)]
for i in range(len(A)):
    A[i]=interval(A[i][0],A[i][1])
fuzzy_quicksort(A,0,7)
for i in A:
    print(i.left,i.right,sep=',',end='  ')
