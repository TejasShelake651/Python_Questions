#Stopword Removal
s = input("enter paragraph: ")

stopwords = ["is","am","are","the","a","an","and","or","of","to","in","on","for","with"]

words = s.split()
ans = ""

for i in words:
    if i.lower() not in stopwords:
        ans += i + " "

print(ans)



#Sentence Segmentation
import re

s = input("enter text: ")

abbreviations = ["Dr.","Mr.","Mrs.","Ms.","Prof."]

for i in abbreviations:
    s = s.replace(i,i.replace(".","<DOT>"))

sentences = re.split(r"[.!?]+",s)

for i in sentences:
    i = i.replace("<DOT>",".")

    if i.strip() != "":
        print(i.strip())



#Text Summarizer
s = input("enter text: ")

sentences = s.split(".")

words = s.lower().split()

frequency = {}

for i in words:
    if i in ["the","is","a","an","and","of","to","in","for","on"]:
        continue

    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

scores = []

for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        if word in frequency:
            score += frequency[word]
    scores.append((score,sentence.strip()))

scores = sorted(scores,reverse=True)

print("summary:")

for i in range(min(3,len(scores))):
    if scores[i][1] != "":
        print(scores[i][1])



#NLP Text Normalization
import re

s = input("enter text: ")

contractions = {
    "don't":"do not",
    "can't":"cannot",
    "won't":"will not",
    "isn't":"is not",
    "aren't":"are not",
    "wasn't":"was not",
    "weren't":"were not",
    "I'm":"I am",
    "I've":"I have",
    "I'll":"I will"
}

for i in contractions:
    s = s.replace(i,contractions[i])

s = s.lower()
s = re.sub(r"[^a-zA-Z\s]","",s)
s = re.sub(r"\d+","",s)

print(s)



#Keyword Extraction
s = input("enter text: ")

stopwords = ["the","is","a","an","and","or","of","to","in","for","on","with","this","that"]

words = s.lower().split()

frequency = {}

for i in words:
    i = i.strip(".,!?;:")
    if i not in stopwords and i != "":
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] =1

sorted_words = sorted(frequency.items(),key=lambda x:x[1],reverse=True)

print("top 5 keywords:")

for i in range(min(5,len(sorted_words))):
    print(sorted_words[i][0],"=",sorted_words[i][1])



#Simple Spell Checker
text = input("enter text: ")

dictionary = {
    "this","is","a","simple","text","hello","world","python",
    "program","student","computer","science","book","school",
    "college","good","bad","example","programming","language"
}

words = text.lower().split()
misspelled = []

for i in words:
    i = i.strip(".,!?;:")

    if i not in dictionary and i not in misspelled:
        misspelled.append(i)

print("misspelled words =",misspelled)
