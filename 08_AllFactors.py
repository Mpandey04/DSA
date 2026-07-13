from math import sqrt
n=int(input("Give any number for factors\n"))
num=n
factors=[]
for i in range(1,num+1):
    if(num%i==0):
        factors.append(i)
        
print(f"Factors of number {n} is: {factors}")

#Time complexity would be: O(n)
# space complexity would be: O(k) where k is the number of factors.


def betterApproachForFactor(num):
    factors=[]
    for i in range(1,int((num/2)+1)):
        if (num%i==0):
            factors.append(i) 
    factors.append(num)  
    return factors
            
print(betterApproachForFactor(n))

#Time complexity=O(n/2)~~O(n)
# space complexity=O(k)

