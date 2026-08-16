# Simple method
def is_palindrome(s):
    return s == s[::-1]
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
  
# using for loop
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")

"""using functions and 2 pointers 
and its a Best way 
"""
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
