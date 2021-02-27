# original

x1 = str(5.3)
x2 = str(5.1)
print("x1 = " + x1)
print("x2 = " + x2)

# better variants

x1 = 5.33123213
x2 = 5.1

# print with args
print("x1 =", x1)
print("x2 =", x2)

# string formating
# C-style
print("x1 = %.2f" % x1)
print("x2 = %.2f" % x2)

# .format()
print("x1 = {0}".format(x1))
print("x2 = {root2}".format(root2=x2))

# f-string
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2}")
