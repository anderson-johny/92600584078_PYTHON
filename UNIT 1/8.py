print('==================Mutable and Immutable Objects==================')

x=[10,20,30]
print('Original List                :',x)
x[1]=50
print('Updated List                 :',x)

student={'name':'Rahul','age':20}
print('Original Dictionary          :',student)
student['age']=21
print('Updated Dictionary           :',student)

print('==================Immutable Objects===========================')
y=(10,20,30)
print('Original Tuple               :',y)
# y[1]=50, Tuple not support

print('Tuple after operation        :',y)

name='Python'
print('Original String              :',name)

# name[0]='J', String cannot be changed
name=name.replace('P','J')
print('New String                   :',name)
a=10
print('Original Integer             :',a)
a=a+5
print('New Integer                  :',a)
