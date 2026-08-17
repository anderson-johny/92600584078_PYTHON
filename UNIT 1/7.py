print('===================DICTIONARY METHODS AND ITERATION=================')

student={
'name':'Anderson',
'middle':'Johny',
"class" : "MCA",
'age':'21',
}
print('Dictionary          :',student)
print('\nLength              :',len(student))
print("\nString              :",str(student))
new_s=student.copy()
print("\nCopied Dictionary   :",new_s)
print("\nItems               :",student.items())
print('\nKeys                :',student.keys())
print('\nValues              :',student.values())
print('\n=====================ITERATION=====================')
for key in student:
    print('Key                 :',key)
for value in student.values():
    print('Value               :',value)
for key,value in student.items():
    print('Key and Value       :',key,value)
student.clear()
print("\nAfter clear()         :",student)