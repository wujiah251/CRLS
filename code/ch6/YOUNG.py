'''
Young氏矩阵
'''

class Young_matrix:

    def __init__(self,A,m,n):
        self.m=m
        self.n=n
        self.matrix=[[float("inf")]*n for i in range(m)]
        self.young_build_heap(A)

    def young_min_heapify(self,i,j):
        if i<self.m-1 and j<self.n-1:
            if self.matrix[i][j]>self.matrix[i+1][j] and self.matrix[i+1][j]<self.matrix[i][j+1]:
                tmp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[i+1][j]
                self.matrix[i+1][j]=tmp
                self.young_min_heapify(i+1,j)
            if self.matrix[i][j]>self.matrix[i][j+1] and self.matrix[i][j+1]<self.matrix[i+1][j]:
                tmp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[i][j+1]
                self.matrix[i][j+1]=tmp
                self.young_min_heapify(i,j+1)
            return
        if i==self.m-1:
            if self.matrix[i][j]>self.matrix[i][j+1]:
                tmp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[i][j+1]
                self.matrix[i][j+1]=tmp
                self.young_min_heapify(i,j+1)
            return
        if j==self.n-1:
            if self.matrix[i][j]>self.matrix[i+1][j]:
                tmp=self.matrix[i][j]
                self.matrix[i][j]=self.matrix[i+1][j]
                self.matrix[i+1][j]=tmp
                self.young_min_heapify(i+1,j)
            return
        return

    def young_extract_min(self):
        min=self.matrix[0][0]
        self.matrix[0][0]=float("inf")
        self.young_min_heapify(0,0)

    def young_decrease_key(self,i,j,key):
        if self.matrix[i][j]<=key:
            exit(-1)
        self.matrix[i][j]=key
        while True:
            if i>=1 and j>=1:
                if self.matrix[i-1][j]>self.matrix[i][j] and self.matrix[i-1][j]>=self.matrix[i][j-1]:
                    self.matrix[i][j]=self.matrix[i-1][j]
                    self.matrix[i-1][j]=key
                    i-=1
                elif self.matrix[i][j-1]>self.matrix[i][j] and self.matrix[i][j-1]>=self.matrix[i-1][j]:
                    self.matrix[i][j]=self.matrix[i][j-1]
                    self.matrix[i][j-1]=key
                    j-=1
                else:return
            elif i==0 and j==0:
                return
            elif i==0:
                if self.matrix[i][j-1]>self.matrix[i][j]:
                    self.matrix[i][j]=self.matrix[i][j-1]
                    self.matrix[i][j-1]=key
                    j-=1
                else:
                    return
            else:
                if self.matrix[i-1][j]>self.matrix[i][j]:
                    self.matrix[i][j]=self.matrix[i-1][j]
                    self.matrix[i-1][j]=key
                    i-=1
                else:
                    return

    def young_insert_key(self,key):
        if self.matrix[self.m-1][self.n-1]<float("inf"):
            matrix=self.matrix.copy()
            self.m+=1
            self.n+=1
            self.matrix=[[float("inf")]*self.n for i in range(self.m)]
            for i in range(self.m-1):
                for j in range(self.n-1):
                    self.matrix[i][j]=matrix[i][j]
            self.matrix[self.m-1][self.n-1]=key+1
            self.young_decrease_key(self.m-1,self.n-1,key)
        self.matrix[self.m-1][self.n-1]=key+1
        self.young_decrease_key(self.m-1,self.n-1,key)

    def young_build_heap(self,A):
        for i in range(len(A)):
            self.young_insert_key(A[i])
        
    def young_find(self,key):
        return self.young_find_location(0,0,key)
    
    def young_find_location(self,i,j,key):
        if self.matrix[i][j]==key:
            return True
        if i>=self.m or j>=self.n or self.matrix[i][j]>key:
            return False
        if self.young_find_location(i,j+1,key):
            return True
        elif self.young_find_location(i+1,j,key):
            return True
        else:
            return False
        


a=[9,6,3,2,4,8,5,14,12]
matrix=Young_matrix(a,4,4)
print(matrix.matrix)
print(matrix.young_find(8))