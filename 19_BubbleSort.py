# Bubble short is basically adjacent swap
n=int(input("What should be your length for your array or list between 1 to 10\n"))
li=[]
for i in range(1,n+1):
    num=int(input((f"Enter {i} element:")))
    li.insert(i,num)
    
print(li)
def BubbleSort(arr):
    n=len(arr)    
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
print("="*40)
BubbleSort(li)
print(BubbleSort[1,6,8,10,12])

#Time complexity=O(n(n+1)/2)
# Space complexity=O(1)