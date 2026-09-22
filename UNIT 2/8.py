x = 10

def outer():
    y = 20 

    def inner():
        nonlocal y
        y += 5
        print("Nonlocal y =", y)

    inner()

def local():
    z = 30   
    print("Local z =", z)

local()
print("Global x =", x)
outer()