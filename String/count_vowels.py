# count vowels in a string using a function
# USING FOR-LOOP
def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

# if you convert the input to lowercase
def count_vowels(s):
    s = s.lower()
    count = 0
    for char in s:
        if char in "aeiou":
            count += 1
    return count
