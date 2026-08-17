print("=====================Data Types And Type Casting=================")
x = 10
y = 10.5
z = x + 3j
a = 'hello'
b = True
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {'name': 'John', 'age': 20}
print('INTEGER     :', x, type(x))
print('FLOAT       :', y, type(y))
print('COMPLEX     :', z, type(z))
print('STRING      :', a, type(a))
print('BOOLEAN     :', b, type(b))
print('LIST        :', c, type(c))
print('TUPLE       :', d, type(d))
print('SET         :', e, type(e))
print('DICTIONARY  :', f, type(f))
print("\n===================== Type Casting =====================")
x = 10
x = float(x)
print('Integer to Float :', x, type(x))
y = 10.5
y = int(y)
print('Float to Integer :', y, type(y))
x = 10.5
x = str(x)
print('Float to String  :', x, type(x))
a = '25'
a = int(a)
print('String to Integer:', a, type(a))
b = '15.5'
b = float(b)
print('String to Float   :', b, type(b))
c = 1
c = bool(c)
print('Integer to Boolean:', c, type(c))