"""
10. Write a program that counts the frequency of each character in a given string. The program should:
● Count how many times each character (including spaces and punctuation) appears in the string.
● Display the frequency of each character in descending order of frequency.
● Allow the user to ignore case or make it case-sensitive.
Tasks:
● Use a dictionary to store the frequency of each character.
● Sort the dictionary by frequency in descending order.
"""

def char_frequency(text, ignore_case=False):
    if ignore_case:
        text = text.lower()
        
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
        
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_freq:
        print(f"'{char}': {count}")

char_frequency("Hello World", ignore_case=True)
