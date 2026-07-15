def func(x,n):
    if(n==0):
        return 
    print(x)
    func(x,n-1)
    
# func(20,10)

def printOneToN(i,num):
    if(i>num):
        return
    print(i)
    printOneToN(i+1,num)
    
# printOneToN(10,50)