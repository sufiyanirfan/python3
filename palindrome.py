def isPalindrome(s):
    return s == s[::-1]
  
s = "madam"
ans = isPalindrome(s)
 
if ans:
    print("Yes, the string is palindrome")
else:
    print("No, the string is not palindrome")
