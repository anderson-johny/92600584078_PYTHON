
import re
import os

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "data.txt")
with open(file_path, "r") as file:
    text = file.read()

print("Text from file:")
print(text)

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

phones = re.findall(r'\b\d{10}\b', text)

print("Email Addresses:", emails)
print("Phone Numbers:", phones)
