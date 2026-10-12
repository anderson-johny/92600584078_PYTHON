import shutil
import os

with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

print("File created successfully")

shutil.copy("sample.txt", "copy.txt")
print("File copied successfully")
shutil.move("copy.txt", "moved.txt")
print("File moved successfully")

os.remove("moved.txt")
print("File deleted successfully")

os.remove("sample.txt")
print("Original file deleted successfully")