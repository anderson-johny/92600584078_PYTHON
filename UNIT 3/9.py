import re

text = "Python is easy. Python is powerful."

pattern = "Python"

result1 = re.match(pattern, text)
if result1:
    print("Match:", result1.group())
else:
    print("No match found at the beginning")

result2 = re.search(pattern, text)
if result2:
    print("Search:", result2.group())
else:
    print("Pattern not found")

result3 = re.findall(pattern, text)
print("Find all:", result3)