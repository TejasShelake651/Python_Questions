"""
6. Write a program to analyze the vocabulary used in two different books. You need to:
● Find all unique words used in each book.
● Identify the common words between both books.
● Identify words that are unique to each book (not found in the other book).
● Display the total number of unique words across both books.
Tasks:
● Use sets to find the unique words in each text, and perform set operations to find the union, intersection, and differences.
"""

book1_text = "hello world from the first book"
book2_text = "hello from the second book"

words1 = set(book1_text.split())
words2 = set(book2_text.split())

print("Unique in book1:", words1)
print("Unique in book2:", words2)
print("Common:", words1 & words2)
print("Only in book1:", words1 - words2)
print("Only in book2:", words2 - words1)
print("Total unique:", len(words1 | words2))
