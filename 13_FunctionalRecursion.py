# total=0
# def sumOfNaturalNumber(num):
#     global total
#     if(num==0):
#         return
#     sumOfNaturalNumber(num-1)
#     print(num,end=" , ")
#     total=total+num
#     return total
    
# print(f"Total sum:",sumOfNaturalNumber(10))


def sumOfNaturalNumber(sum,i,n):
    if(i>n):
        print(f"sum of first {n} natural number is: {sum} ")
        return
    sumOfNaturalNumber(sum+i,i+1,n)
    
sumOfNaturalNumber(0,1,10)

#Function Recursion
#1. create a flow
#2. create the base condition

def sumofNaturalNUmberUsingFunctionCall(n):
    if(n==1):
        return 1
    return n+sumofNaturalNUmberUsingFunctionCall(n-1)