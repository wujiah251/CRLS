
def insert_sort(A):
    n=len(A)
    for i in range(1,n):
        key=A[i]
        j=i-1
        while j>=0 and key <A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

def buck_sort(A):
    n=len(A)
    B=[[] for i in range(n)]
    for i in range(n):
        B[int(n*(A[i]))].append(A[i])
    for i in range(n):
        insert_sort(B[i])
    k=0
    
    for i in range(n):
        length=len(B[i])
        for j in range(length):
            A[k]=B[i][j]
            k+=1

A=[0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
buck_sort(A)
print(A)
