import math
print("1. Import entire module:")
print("Square root of 25 =", math.sqrt(25))

from math import factorial
print("\n2. Import specific function:")
print("Factorial of 5 =", factorial(5))

from math import pow
print("\n3. Import multiple functions:")
print("2 raised to 3 =", pow(2, 3))

import math as m
print("\n4. Import module with an alias:")
print("Value of pi =", m.pi)

from math import sqrt as square_root
print("\n5. Import function with an alias:")
print("Square root of 49 =", square_root(49))

from math import *
print("\n6. Import all functions:")
print("Sine of 0 =", sin(0))
print("GCD of 12 and 18 =", gcd(12, 18))