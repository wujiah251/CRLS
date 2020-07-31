'''
栈
'''

class stack:
    def __init__(self,size=10):
        self.size=size
        self.array=[None for i in range(size)]
        self.top_i=-1

    def top(self):
        if self.top_i==-1:
            print("the stack is empty!")
            return None
        return self.array[self.top_i]

    def isempty(self):
        if self.top_i==-1:
            return True
        else:
            return False
    

    def doublespace(self):
        temp=[None for i in range(self.size*2)]
        for i in range(self.size):
            temp[i]=self.array[i]
        self.array=temp
        self.size=self.size*2


    def push(self,key):
        if self.top_i==self.isemptysize-1:
            self.doublespace()
        self.top_i=self.top_i+1
        self.array[self.top_i]=key

    def pop(self):
        if self.top_i==-1:
            print("the stack is empty!")
            return None
        self.top_i=self.top_i-1
        return self.array[self.top_i+1]


A=[1,2,3,4,5,6,7,8,9,10,11,12]
length=len(A)
Stack=stack()
for i in range(length):
    Stack.push(A[i])
for i in range(length):
    print(Stack.pop(),end=' ')
