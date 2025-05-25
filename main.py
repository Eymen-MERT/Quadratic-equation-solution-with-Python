import cmath
import math

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

delta = b**2 - 4*a*c
print(f"{a}x² + {b}x + {c} = 0")
print(f"Delta = {delta}")

if delta < 0:

    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

elif delta == 0:

    x = -b / (2*a)

    print(f"x = {x}")

else:

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
