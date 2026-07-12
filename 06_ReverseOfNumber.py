n=int(input("Give any number for checking palindrome\n"))
num=n
reverse=0
while num>0:
    ld=num%10
    reverse=(reverse*10)+ld
    num=num//10
    
if(n==reverse):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
    
#Time complexity- O(log(n))
#space complexity- O(1)