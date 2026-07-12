from math import floor,log10
n=int(input("Give number for checking armstrong number\n"))
num=n
def numberOfDigit(num):
    if(num==0):
        return 1
    return floor(log10(num)+1)

nod=numberOfDigit(n)


def armstrong(num):
    total=0
    while num>0:
        ld=num%10
        total=total+(ld**nod)
        num=num//10     
    return total

isArmstrong=armstrong(n)

if (n==isArmstrong):
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is not a armstrong number")