str=input("Enter your word for checking palindrome\n")
def palindrome(str,left,right):
    if(left>=right):
        return True
    if(str[left]==str[right]):
        palindrome(str,left+1,right-1)
    else:
        return False
    
  
palindrome(str.lower(),0,len(str)-1)