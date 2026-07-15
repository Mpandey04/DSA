# A function call itself

#Head Recursion
count=0
def callName():
    global count
    if(count==4):
        return
    print("Manish")
    count+=1
    callName()
    
callName()


#Tail Recursion: Tail recursion me pahle function call hoga phir uske baad apka jo job hai wo hoga.

#time complexity -> O(n+1)->O(n)
# Space complexity-> O(n+1)->O(n)