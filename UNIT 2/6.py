print('=================DEMONSTRATING LIST USING LOOP====================')
x= ['ABC','DEF','GHI','JKL']

for i in x:
    print(i)
print('=================DEMONSTRATING STRING USING LOOP====================')
z='PYTHON'
for i in z:
    print(i)
print('=================DEMONSTRATING DICTIONARY USING LOOP====================')

y={'Name:':'ANDERSON',
   'M.NAME:':'JOHNY',
   'L.NAME:':'GEORGE',
   'ROLLNUMBER:':'4078',
   }

for key,value in y.items():
    print(key, value)