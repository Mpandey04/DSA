def Fibbonacci(num):
    if (num==0 or num==1):
        return num
    return Fibbonacci(num-1)+Fibbonacci(num-2)


# ye pure series ko print karta hai
n = int(input("Enter number of terms: "))
for i in range(n):
    print(Fibbonacci(i), end=" ")
    
    
#Time complexity- 2 ki power n
# space complexity- O(n) 