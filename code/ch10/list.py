'''
10.3-2 对一组同构对象用单数组表示法实现
'''

class list:

    def __init__(self,size=10):
        self.size=size
        self.array=[[None,None]for i in range(size)]
        self.L=None
        self.free=0
        for i in range(size-1):
            self.array[i][0]=i+1
        self.array[size-1][0]=None
    
    def free_object(self,x):
        self.array[x]=self.free
        self.free=x
        return 

    def allocate_object(self):
        if self.free==None:
            print("the list is full")
            return None
        x = self.free
        free = self.array[x][0]
        return x
    

'''
10.3-4
紧凑的多重数组的静态双向链表实现
    我们往往希望双向链表的所有元素在存储器中保持紧凑，例如，在多数组表示中占用
前m个下标位置.(在页式虚拟存储的计算环境下，即为这种情况。)假设除指向链表本
身的指针外没有其他指针指向该链表元素，试说明如何实现过程ALLOCATE-OBJECT和
FREE-OBJECT，使得该表示保持紧凑。(提示，使用栈的数组实现)。
'''

class compact_list:

    def __init__(self,MAX=10):
        self.size=MAX
        self.prev=[-1 for i in range(MAX)]
        self.key=[None for i in range(MAX)]
        self.next=[-1 for i in range(MAX)]
        self.head=-1 # 表示没有存储
        self.top=-1 # 栈顶
        self.free=0 # 自由表头节点为0

    def allocate_object(self):
        if self.top==self.size-1:
            pritn("the list is full!")
            return None
        self.top=self.top+1
        self.free=self.top+1
        x=self.top
        # 新分配的空间作为list的head
        self.prev[x]=-1 
        self.next[x]=self.head
        if self.head!=-1:
            self.prev[self.head]=x
        self.head=x
        return x

    def free_object(self,x):
        if x>self.top:
            return
        
        self.key[x]=self.key[self.top]
        self.next[x]=self.next[self.top] if self.next[self.top]!=x else self.next[x]
        self.prev[x]=self.prev[self.top] if self.prev[self.top]!=x else self.prev[x]
        if self.prev[x]!=-1:
            self.next[self.prev[x]]=x
        if self.next[x]!=-1:
            self.prev[self.next[x]]=x
        if self.head==self.top:
            self.head=x
        self.top=self.top-1
        self.free=self.free-1

    def insert(self,key):
        x=self.allocate_object()
        if x==None:
            return
        self.key[x]=key

    def search(self,key):
        temp=self.head
        while temp!=-1:
            if self.key[temp]==key:
                return temp
            else:
                temp=self.next[temp]
        return None

    def delete(self,key):
        x=self.search(key)
        if x==None:
            return
        else:
            self.free_object(x)
            return
    
    def __str__(self):
        temp=self.head
        Str=''
        for i in range(self.top):
            Str=Str+str(self.key[temp])+'->'
            temp=self.next[temp]
        Str=Str+str(self.key[temp])
        return Str

T=compact_list(10)
List=[0,1,2,3,4,5,6,7]
for i in range(8):    
    T.insert(List[i])
for i in range(4):
    T.free_object(i)
print(T)



'''
10.3-5
    设L是一个长度为n的双向链表，存储于长度为m的数组key,prev和next中。
假设这些数组由维护双链自由表F的两个过程ALLOCATE-OBJECT和FREE-OBJECT
进行管理。又假设m个元素中，恰有n个元素在链表L上，m-n个在自由表上。给
定链表L和自由表F，试写出一个过程COMPACTIFY-LIST(L,F),用来移动L的元
素使其占用数组中1,2，。。。n的位置，调整自由表F以保持其正确性，并且
占用数组中n+1,n+2....,m的位置。要求缩写的过程运行时间应为 θ(n)，且
只使用固定量的额外存储空间。请证明所写的过程是正确的。
'''

class Double_List:
    def __init__(self,size=10):
        self.size=size
        self.prev=[i-1 for i in range(size)]
        self.key=[None for i in range(size)]
        self.next=[i+1 for i in range(size)]
        self.flag=[False for i in range(size)] #表示没有被占用
        self.next[size-1]=-1 # 表示下一节点为空
        self.head=-1 # 内存头节点
        self.free=0 # 自由表头节点
        self.length=0 # 内存长度
    
    def allocate_object(self):
        if self.length>self.size:
            print("the list is full")
            return
        x=self.free
        self.free=self.next[x]
        self.flag[x]=True
        self.length=self.length+1
        if self.free!=-1:
            self.prev[self.free]=-1
        self.next[x]=self.head
        if self.head!=-1:
            self.prev[self.head]=x
        self.head=x
        return x

    def free_object(self,x):
        if x<0 or x>=self.size:
            return
        if self.flag[x]==False:
            return
        self.flag[x]=False
        self.length=self.length-1
        self.key[x]=None # 可不加，为了便于检验
        if self.prev[x]!=-1:
            self.next[self.prev[x]]=self.next[x]
        if self.next[x]!=-1:
            self.prev[self.next[x]]=self.prev[x]
        # x被设置为自由表头节点
        self.prev[x]=-1
        self.next[x]=self.free
        if self.free!=-1:
            self.prev[self.free]=x
        self.free=x
    def compactify_list(self):
        # 左右指针
        left=0
        right=self.size-1
        while left<right:
            while self.flag[left]==True and left<right:
                left=left+1
            while self.flag[right]==False and left<right:
                right=right-1
            if left<right:
                key=self.key[left]
                self.key[left]=self.key[right]
                self.key[right]=key
                self.flag[left]=True
                self.flag[right]=False
                if self.head==right:
                    self.head=left
                else:
                    self.next[self.prev[right]]=left
                if self.next[right]!=-1:
                    self.prev[self.next[right]]=left
                if self.free==left:
                    self.free=right
                else:
                    self.next[self.prev[left]]=right
                if self.next[left]!=-1:
                    self.prev[self.next[left]]=right
                temp=self.prev[left]
                self.prev[left]=self.prev[right]
                self.prev[right]=temp
                temp=self.next[left]
                self.next[left]=self.next[right]
                self.next[right]=temp
                left=left+1
                right=right-1
        return
        


T=Double_List(10)
List=[0,1,2,3,4,5,6,7]
for i in range(8):    
    x=T.allocate_object()
    T.key[x]=List[i]
for i in range(4):
    T.free_object(i)

print(T.head,T.free,T.length)
print(T.prev)
print(T.key)
print(T.next)
T.compactify_list()
print(T.head,T.free,T.length)
print(T.prev)
print(T.key)
print(T.next)

