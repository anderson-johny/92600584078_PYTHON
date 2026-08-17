print('===================USER DEFINED FUNCTIONS=================')
def hello():
    print('Hello, Welcome to Python')

hello()
def add(a,b):
    print('Addition            :',a+b)
add(10,20)

def greet(name='Student'):
    print('Name                :',name)
greet()
greet('Anderson')

def student(name,age):
    print('Student Name        :',name)
    print('Student Age         :',age)

student(age=21,name='Anderson')

def numbers(*args):
    print('Arguments            :',args)

numbers(10,20,30,40,50)

def multiply(a,b):
    return a*b

result=multiply(5,4)
print('Multiplication       :',result)