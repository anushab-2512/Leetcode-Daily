# Use a set for duplicates
def find_duplicates(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return duplicates
text = input("Enter a string: ")
result = find_duplicates(text)
print("Duplicate characters:", result)

# Use a list for duplicates
def find_duplicates(s):
    seen = set()
    duplicates = []
    for char in s:
        if char in seen:
            if char not in duplicates:
                duplicates.append(char)
        else:
            seen.add(char)
    return duplicates
