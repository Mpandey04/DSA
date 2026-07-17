num=int(input("What should be size of your list between 1 to 10:"))
li=[]
for i in range(0,num):
    n=int(input(f"Enter {i} element:"))
    li.insert(i,n)
    
def insertionSort(arr):
    n=len(arr)
    index=0
    for i in range(1,n):
        index=arr[i]
        j=i-1
        while (j>=0 and arr[j]>index):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=index

print(li)
print("="*50)
insertionSort(li)


# Time Complexity-O(n(n+1)/2)~~O(N square)
# Space complexity-