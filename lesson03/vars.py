# original

import sys

hypotenuse = (float(sys.argv[1])**2+float(sys.argv[2])**2)**(1/2)

print("Length of hypotenuse is", hypotenuse)

# corrected

a = float(sys.argv[1])
b = float(sys.argv[2])

hypotenuse = (a**2 + b**2)**(1/2)

print(hypotenuse)
