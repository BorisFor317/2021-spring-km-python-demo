import math

from sqrt import square_root


test_data = [
    4,
    16,
    2**32,
    2**64,
    111325,
    111111111111111111111111111111111111111111111111111111111111111
]

for x in test_data:
    my_sqrt = square_root(x)
    real_sqrt = math.sqrt(x)

    err = abs(my_sqrt - real_sqrt)

    print(f"for {x} sqrt is equal to {real_sqrt:4f}.")
    print(f"my method result {my_sqrt}")
    print(f"abs error of my method is {err}.")
    print(f"rel error of my method is {err / real_sqrt}.\n")
