x=[1,2,3,4,5]
square_list=[i**2 for i in x]
square_dict={i:i**2 for i in x}
square_set={i**2 for i in x}
print('LIST COMPREHENSIONS:',square_list)
print('DICTIONARY COMPREHENSIONS:',square_dict)
print('SET COMPREHENSIONS:',square_set)