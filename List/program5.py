"""
5. Write a program to build a simple text analysis tool. The tool should perform the following operations on a given paragraph of text:
● Count the total number of words.
● Count the frequency of each word.
● Identify and display the top 3 most frequent words.
● Count the number of vowels in the entire text.
Tasks:
● Use string manipulation to split the text into words and to check for vowels.
● Use a dictionary to store the word frequencies.
"""

def analyze_text(text):
    words = text.lower().split()
    print("Total words:", len(words))

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 words:", top3)

    vowels = "aeiou"
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    print("Vowels:", vowel_count)

text = "This is a simple text. Text is simple but this is text."
analyze_text(text)
