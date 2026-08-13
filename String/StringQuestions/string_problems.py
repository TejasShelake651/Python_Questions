# 1 Word Count
from collections import Counter
import re
import string

def word_count(s: str) -> int:
    return len(s.split())

# 2 Longest Word
def longest_word(s: str) -> str:
    words = s.split()
    return max(words, key=len) if words else ""

# 3 Shortest Word
def shortest_word(s: str) -> str:
    words = s.split()
    return min(words, key=len) if words else ""

# 4 Title Case
def to_title_case(s: str) -> str:
    return s.title()

# 5 Duplicate Characters
def duplicate_characters(s: str) -> set:
    c = Counter(s)
    return {ch for ch, cnt in c.items() if cnt > 1}

# 6 Character Frequency
def char_frequency(s: str) -> dict:
    return dict(Counter(s))

# 7 Anagram Check
def are_anagrams(a: str, b: str) -> bool:
    a_clean = re.sub(r"\s+", "", a).lower()
    b_clean = re.sub(r"\s+", "", b).lower()
    return Counter(a_clean) == Counter(b_clean)

# 8 Remove Duplicate Characters (preserve order)
def remove_duplicate_chars(s: str) -> str:
    seen = set()
    out = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            out.append(ch)
    return ''.join(out)

# 9 Substring Search (returns first index or -1)
def substring_search(text: str, sub: str) -> int:
    return text.find(sub)

# 10 Count Occurrences of a Word (case-insensitive, word boundaries)
def count_word_occurrences(text: str, word: str) -> int:
    words = re.findall(r"\b" + re.escape(word) + r"\b", text, flags=re.IGNORECASE)
    return len(words)

# 11 Password Validator
def validate_password(pw: str) -> bool:
    if len(pw) < 8:
        return False
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"[a-z]", pw):
        return False
    if not re.search(r"[0-9]", pw):
        return False
    if not re.search(r"[{}]".format(re.escape(string.punctuation)), pw):
        return False
    return True

# 12 Run-Length Encoding
def run_length_encode(s: str) -> str:
    if not s:
        return ""
    out = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            out.append(f"{prev}{count}")
            prev = ch
            count = 1
    out.append(f"{prev}{count}")
    return ''.join(out)

# 13 String Compression (return original if not shorter)
def string_compress(s: str) -> str:
    comp = run_length_encode(s)
    return comp if len(comp) < len(s) else s

# 14 Most Frequent Character
def most_frequent_char(s: str) -> str:
    if not s:
        return ''
    return Counter(s).most_common(1)[0][0]

# 15 Second Most Frequent Character
def second_most_frequent_char(s: str) -> str:
    freq = Counter(s).most_common()
    return freq[1][0] if len(freq) > 1 else ''

# 16 Caesar Cipher (encrypt/decrypt)
def caesar_encrypt(plaintext: str, shift: int) -> str:
    def shift_char(ch):
        if 'a' <= ch <= 'z':
            return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        if 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        return ch
    return ''.join(shift_char(ch) for ch in plaintext)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)

# 17 Email Validator (basic)
def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 18 Word Frequency Dictionary
def word_frequency(text: str) -> dict:
    words = re.findall(r"\w+", text.lower())
    return dict(Counter(words))

# 19 Sentence Reversal (reverse word order)
def reverse_sentence(s: str) -> str:
    return ' '.join(s.split()[::-1])

# 20 String Rotation (check if s2 is rotation of s1)
def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)


if __name__ == '__main__':
    # Minimal demonstration (change calls below to test functions)
    s = input('Enter a sample string for tests: ')
    print('Word count:', word_count(s))
    print('Longest word:', longest_word(s))
    print('Shortest word:', shortest_word(s))
    print('Title case:', to_title_case(s))
    print('Duplicate chars:', duplicate_characters(s))
    print('Char freq:', char_frequency(s))
