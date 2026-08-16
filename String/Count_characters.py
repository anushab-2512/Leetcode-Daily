# count the number of characters in a string using a function
# without using len()
def count_characters(s):
    count = 0
    for char in s:
        count += 1
    return count
text = input("Enter a string: ")
print("Number of characters:", count_characters(text))

# by using len ()
def count_characters(s):
    return len(s)
text = input("Enter a string: ")
print("Number of characters:", count_characters(text))
