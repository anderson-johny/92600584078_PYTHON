
import re

text = "Python programming is easy"

pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found")
    print("Matched pattern:", result.group())
else:
    print("Pattern not found")
