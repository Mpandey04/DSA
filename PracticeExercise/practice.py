n=int(input("Enter number for digit count\n"))
count=0
num=n
while(num>0):
    count+=1
    num=num//10
    
print("Total number of digit:",count)

