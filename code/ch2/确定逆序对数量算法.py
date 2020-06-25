'''算法导论习题2-4'''

def compute_reverse(a,size):
    b=a.copy()
    result=compute_reverse_internal(b,0,size//2-1)+compute_reverse_internal(b,size//2,size-1)
    result+=compute_reverse_external(b,0,size//2-1,size//2,size-1)
    return result


def compute_reverse_external(a,start1,end1,start2,end2):
    result = 0
    len2=end2-start2+1
    j=0
    for i in range(start1,end1+1):
        while j<len2 and a[i]>a[start2+j]:
            result+=(end1+1-i)
            j+=1
        if j==len2:
            return result
    return result

def compute_reverse_internal(a,start,end):
    if start==end:
        return 0
    if end-start==1:
        if a[start]>a[end]:
            tmp=a[start]
            a[start]=a[end]
            a[end]=tmp
            return 1
        else:
            return 0
    len = end - start + 1 
    start1=start
    end1=start+len//2-1
    start2=end1+1
    end2=end
    result = compute_reverse_internal(a,start1,end1)+compute_reverse_internal(a,start2,end2)
    result += compute_reverse_external(a,start1,end1,start2,end2)
    # 归并排序
    tmp=[0]*len
    k1=start
    k2=start+len//2
    for i in range(0,len):
        if  k1<=end1 and k2<=end2:
            if a[k1]<a[k2]:
                tmp[i]=a[k1]
                k1+=1
            else:
                tmp[i]=a[k2]
                k2+=1
        elif k1<end1:
            tmp[i]=a[k1]
            k1+=1
        else:
            tmp[i]=a[k2]
            k2+=1
    for i in range(0,len):
        a[start+i]=tmp[i]
    return result

a=[7,3,6,8,1,3,4,6,7,11]
print(compute_reverse(a,len(a)))