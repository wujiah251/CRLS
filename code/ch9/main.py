
def f(x):
    print("here")
    return 2*x+1

def print_(x,k):
    for i in x:
        print(i)
    if k==1:
        return 
    print(1)

a=print_([0,1,2],2)
print(a)