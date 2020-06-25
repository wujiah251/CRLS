'''
计数排序
'''

def counting_sort(A,B,k):
    C=[0]*(k+1)
    for i in range(k+1):
        C[i]=0
    for j in range(len(A)):
        C[A[j]]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1

A=[8,7,6,6,5,5,4,3,2,1]
B=[0]*len(A)
counting_sort(A,B,8)
print(B)