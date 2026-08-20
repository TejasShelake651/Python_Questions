"""
8. Write a program to check if two given strings are anagrams. Two strings are anagrams if they contain the same characters in the same frequency but in a different order (e.g., "listen" and "silent"). The program should:
● Accept two strings as input.
● Ignore spaces, case, and punctuation.
● Determine if the two strings are anagrams of each other.
Tasks:
● Use string manipulation to normalize the strings by removing spaces, converting to lowercase, and ignoring punctuation.
● Use sets or dictionaries to compare the frequency of characters in both strings.
"""

def is_anagram(s1, s2):
    def clean(s):
        return "".join(c.lower() for c in s if c.isalnum())
    
    clean1 = clean(s1)
    clean2 = clean(s2)

    return sorted(clean1) == sorted(clean2)

print("listen & silent:", is_anagram("listen", "silent"))
print("hello & world:", is_anagram("hello", "world"))
