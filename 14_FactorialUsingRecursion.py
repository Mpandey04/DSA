n=int(input("Enter number for factorial\n"))
def Factorial(num):
    if(num==0 or num==1):
        return 1
    return num*Factorial(num-1)

print(f"Factorial of {n} is: {Factorial(n)}")