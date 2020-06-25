'''
d叉堆
'''

class d_heap:

    def __init__(self,A,d):
        self.length=len(A)
        self.array=[0]+A
        self.d=d
        self.build_max_heap()

    def left(self,i):
        return self.d*i-self.d+2

    def right(self,i):
        return self.d*i+1

    def parent(self,i):
        return (i-2)//self.d+1

    def max_heapify(self,i):
        max_i=self.left(i)
        max=self.array[max_i]
        # 子结点由d*i-d+2到d*i+1
        for j in range(self.left(i),min(self.right(i)+1,self.length+1)):
            if self.array[j] > max:
                max_i=j
                max=self.array[j]      
        if max<=self.array[i]:
            return

        self.array[max_i]=self.array[i]
        self.array[i]=max
        if self.left(max_i)>self.length:
            return
        self.max_heapify(max_i)

    def build_max_heap(self):
        for i in range(self.parent(self.length),0,-1):
            self.max_heapify(i)

    def sort(self,flag):
        A=[0]*self.length
        if flag==True:
            for i in range(0,len(A)):
                A[i]=self.array[1]
                self.array[1]=self.array[self.length]
                self.length-=1
                self.max_heapify(1)
        elif flag==False:
            for i in range(len(A)-1,-1,-1):
                A[i]=self.array[1]
                self.array[1]=self.array[self.length]
                self.length-=1
                self.max_heapify(1)
        return A

A=[5,13,2,25,7,17,20,8,4]
heap=d_heap(A,3)
A_sort=heap.sort(False)
print(A_sort)