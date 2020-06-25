'''
基数排序
'''

def index(num,i):
    num=str(num)
    if i>=len(num):
        return 0
    else:
        return int(num[len(num)-i-1])

def radix_sort(A,start,end):
    max=A[start]
    max_i=start
    for i in range(start,end+1):
        if A[i]>max:
            max=A[i]
            max_i=i
        A[i]=str(A[i])
    d = len(A[max_i])
    B = [0]*(end-start+1)
    for i in range(0,d):
        # 比较第i个
        k=0
        # 找到最大数
        for j in range(start,end+1):
            if index(A[j],i)>k:
                k=index(A[j],i)
        C=[0]*(k+1)
        for j in range(start,end+1):
            C[index(A[j],i)]+=1
        for j in range(1,k+1):
            C[j]+=C[j-1]
        for j in range(end,start-1,-1):
            B[C[index(A[j],i)]-1]=A[j]
            C[index(A[j],i)]-=1
        A=B.copy()
    return B

A=[329,457,657,839,436,720,355]
B=radix_sort(A,0,6)
print(B)

