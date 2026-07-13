# Store frequency in dictionary

li=[1,2,4,1,2,5,6,3,4,2,6,4,3,2,7,5,7,5]
nums=li
frequency={}
x=1
for i in range(0,len(nums)):
    if nums[i] in frequency:
        frequency[nums[i]]+=1
    else:
        frequency[nums[i]]=1
        
print(frequency[2])

# Time complexity=O(n)
# Space complexity=O(n)


def HashMap(num):
    hash_map={}
    for i in range(0,len(num)):
        hash_map[num[i]]=hash_map.get(num[i],0)+1
    return hash_map

print(HashMap(nums))