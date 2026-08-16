# Two strings are anagrams if they contain the same characters with the same frequency, but in a different order.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 26
    for char in s1:
        count[ord(char) - ord('a')] += 1
    for char in s2:
        count[ord(char) - ord('a')] -= 1
    for value in count:
        if value != 0:
            return False
    return True
