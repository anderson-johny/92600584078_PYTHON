x=int(input('Enter a Number:'))
def numbers(n):
    for i in range(1, n + 1):
        yield i
for num in numbers(x):
    print(num)
