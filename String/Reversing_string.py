# Simple methods
s = "hello"
print(s[::-1])

# or 
text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)

# By using loops
text = "hello"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)

# using recursion
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

# by using function and 2 pointers 
def reverse_string(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
  
