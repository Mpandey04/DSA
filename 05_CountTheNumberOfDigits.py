from math import log10,floor
n=int(input("Enter any number\n"))
num=n
count=0
while num>0:
    count+=1
    num=num//10

    
print(f"Total number of digits:{count}")

def countOfDigit(num):
    return floor(log10(num)+1)

print(f"Total number of digits: {countOfDigit(n)}")