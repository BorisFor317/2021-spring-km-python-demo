# 

# f = lambda x, y: x**2 + y**2
# print(list(map(f, [1, 2], [1, 2])))


# CONST = 5

# def foo(x, y):
#     result = x**2 + y**2 + CONST
#     print(result)

#     return result


# array = [i**2 for i in range(5)]
# print(array)

# for x, y, z in zip([1, 2], [1, 2], [3, 4]):
#     print(x**2 + y**2)
#     print(z)

# user = "123.221"
# print(user.isdigit())
# print(user.isnumeric())
# print(user.isdecimal())
# print(user.isalnum())

import re

user = "123.221"

if re.match(r'^-?\d+(?:\.\d+)$', user):
    print("is float")
else:
    print("not float")

