import os
import sys

print("Current directory:", os.getcwd())

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully")

with open("MyFolder/sample.txt", "w") as file:
    file.write("Hello, Python!")

print("File created successfully")

print("Directory contents:", os.listdir("MyFolder"))

os.rename("MyFolder/sample.txt", "MyFolder/newfile.txt")
print("File renamed successfully")

print("Python version:", sys.version)

os.remove("MyFolder/newfile.txt")
print("File deleted successfully")

os.rmdir("MyFolder")
print("Directory removed successfully")