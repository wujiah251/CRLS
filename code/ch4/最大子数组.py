'''算法导论4.1最大子数组问题
    分治策略
    4.1.5线性算法
'''


def find_max_subarray(a,size):
    start=0
    end=size-1
    mid=(size-1)//2
    max_start,max_end,max_sum=find(a,start,end)
    return max_start,max_end,max_sum

def find(a,start,end):
    if start==end:
        if a[start]>0:
            return start,end,a[start]
        else:
            return start,start-1,0
    if start>end:
        return start,end,0
    mid=(start+end)//2
    start1=start
    end1=mid-1
    start2=mid+1
    end2=end
    max_start1,max_end1,sum1=find(a,start1,end1)
    max_start2,max_end2,sum2=find(a,start2,end2)
    max_start3,max_end3,sum3=find_max_crossing_subarray(a,start,end,mid)
    if sum1>sum2 and sum1>sum3:
        return max_start1,max_end1,sum1
    elif sum2>sum1 and sum2>sum3:
        return max_start2,max_end2,sum2
    else:
        return max_start3,max_end3,sum3

def find_max_crossing_subarray(a,start,end,mid):
    # 寻找跨越中点的最大子数组
    sum_left=0
    sum_right=0
    max_sum_left=0
    max_sum_right=0
    left=mid-1
    right=mid+1
    max_left=mid
    max_right=mid
    for left in range(mid-1,start-1,-1):
        sum_left+=a[left]
        if sum_left>max_sum_left:
            max_sum_left=sum_left
            max_left=left
    for right in range(mid+1,end+1):
        sum_right+=a[right]
        if sum_right>max_sum_right:
            max_sum_right=sum_right
            max_right=right
    sum=max_sum_left+a[mid]+max_sum_right
    return max_left,max_right,sum


def find(a,size):
    low=0
    high=-1
    max_sum=0
    sum=0
    boundary=0
    index=0
    for j in range(0,size):
        if boundary+a[j]>a[j]:
            boundary+=a[j]
        else:
            boundary=a[j]
            index=j
        if boundary>max_sum:
            low=index
            high=j
            max_sum=boundary
    return low,high,max_sum

A=[13,-33,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
start,end,sum=find(A,len(A))
print(start,end,sum)