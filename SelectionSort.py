num=int(input("How many elements do you want to add in list between 1 to 10:\n"))
li=[]
for i in range(1,num+1):
    n=int(input(f"Enter your {i} element:"))
    li.insert(i,n)    

def selectionSortInAscendingOrder(li):
    
    n=len(li)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if(li[j]<=li[min_index]):
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]


print("Before sorting:",li)
print("="*40)
selectionSortInAscendingOrder(li)
print(li)

#Time complexity: O(n(n+1)/2)~~ O(n2)


def selectionSortInDescendingOrder(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if(arr[min_index]<arr[j]):
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    
print("="*60)
selectionSortInDescendingOrder(li)
print(li)