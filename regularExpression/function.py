import re

txt1 = "Tejas Shelake is a good boy."
match = re.search(r'good', txt1)

if match:
    print(match.group())
    print("Start:", match.start(), "End:", match.end())
else:
    print("No match")

txt2="python is a programming language. Python is used for web development & data analysis."
print(re.findall(r'[Pp]ython', txt2))


string = re.compile(r"\d+")

print(string.search("Age is 21").group())
print(string.search("Marks are 95").group())
print(string.search("Year is 2026").group())