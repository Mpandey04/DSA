#Hashing in python
# Prestoring values into some datastructure like list/dictionary/sets and the fetching it

n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]

# constraints
# 1.1<=n[i]<10
# n can have 10 power 8 elements
# m can have 10 ke power 8 elements.

# for num in m:
#     count=0
#     for x in n:
#         if x==num:
#             count+=1
#     print(f"{num} : {count}")
    
# Time complexity-O(m*n) it will throw TLE error

def hashToList():
    hash_list=[0]*11
    for num in n:
        hash_list[num]+=1
        for nums in m:
            if (nums<1 or nums>10):
                # print(0)
                pass
            else:
                hash_list[nums]
        print(f"{num}:{hash_list[nums]}",end=" ")
    
#Time complexity : O(n+m)
# Space complexity : O(11)

def hashToDict():
    
    # Hashing of n
    hash_n = {}

    for i in n:
        hash_n[i] = hash_n.get(i, 0) + 1

    # Check elements of m in n
    for i in m:
        print(f"{i} occurs {hash_n.get(i, 0)} times in n")
        
hashToDict()
s = "azyxyyxaaaaa"
q = ['d', 'a', 'y', 'z']

def character_hashing():
    has_list = [0] * 26      # a-z ke liye 26 letters

    # Frequency store karna
    for char in s:
        ascii_value = ord(char)
        index = ascii_value - 97
        has_list[index] += 1

    # Query answer
    for ch in q:
        ascii_value = ord(ch)
        index = ascii_value - 97
        print(f"{ch} is : {has_list[index]} times")

character_hashing()