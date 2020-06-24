'''
堆类
'''

class max_heap:
    def __init__(self,a):
        self.size=len(a)
        self.array=a.copy()
        self.build_max_heap()

    def max_heapify(self,i):
        j=2*i+1
        while True:
            if i>=self.size//2:
                return
            if j==self.size-1:
                if self.array[j]>self.array[i]:
                    tmp=self.array[i]
                    self.array[i]=self.array[j]
                    self.array[j]=tmp
                    return
                else:
                    return
            if self.array[i]<self.array[j] or self.array[i]<self.array[j+1]:
                if self.array[j]>self.array[j+1]:
                    tmp=self.array[i]
                    self.array[i]=self.array[j]
                    self.array[j]=tmp
                    i=j
                else:
                    tmp=self.array[i]
                    self.array[i]=self.array[j+1]
                    self.array[j+1]=tmp
                    i=j+1
                j=2*i+1
            else:
                return

    def build_max_heap(self):
        for i in range(self.size//2-1,-1,-1):
            self.max_heapify(i)
        return 

    def heap_maximum(self):
        return self.array[0]
    
    def heap_extract_max(self,):
        max=self.array[0]
        self.array[0]=self.array[self.size-1]
        self.size-=1
        self.max_heapify(0)
        return max

    def heap_increase_key(self,i,key):
        if self.array[i]>=key:
            return
        self.array[i]=key
        while i>0 and self.array[(i-1)//2]<key:
            self.array[i]=self.array[(i-1)//2]
            self.array[(i-1)//2]=key
            i=(i-1)//2
        return

    def max_heap_insert(self,key):
        self.size+=1
        self.array.append(key-1)
        self.heap_increase_key(self.size-1,key)

    def sort(self):
        a=[0]*self.size
        for i in range(self.size-1,0,-1):
            a[i]=self.array[0]
            self.array[0]=self.array[i]
            self.size-=1
            self.max_heapify(0)
        a[0]=self.array[0]
        return a



A=[4,1,3,2,16,9,10,14,8,7]
heap=max_heap(A)
print(heap.array)
heap.max_heap_insert(20)
print(heap.array)