'''
队列
'''

class queue:

    def __init__(self,size=10):
        self.size=size
        self.array=[None for i in range(size)]
        self.head=0
        self.tail=0
        self.length=0

    def doublespace(self):
        temp=[None for i in range(self.size*2)]
        for i in range(self.size):
            temp[i]=self.array[self.head]
            self.head=(self.head+1)%self.size
        self.array=temp
        self.head=0
        self.tail=self.size
        self.size=self.size*2

    def enqueue(self,key):
        if  self.length==self.size:
            self.doublespace()
        self.length=self.length+1
        self.array[self.tail]=key
        self.tail=(self.tail+1)%self.size
    
    def dequeue(self):
        if self.length==0:
            print("the queue is empty!")
        result=self.array[self.head]
        self.head=(self.head+1)%self.size
        self.length=self.length-1


A=[1,2,3,4,5,6,7,8,9,10,11,12]
Queue=queue()
for i in range(5):
    Queue.enqueue(A[i])
for i in range(4):
    Queue.dequeue()
for i in range(5,12):
    Queue.enqueue(A[i])

print(Queue.array,Queue.head,Queue.tail)