# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
def square_root(value, abs_err=1e-9, iters=10000):
    current = (value + 1) / 2
    err = 1
    count = 0
    while count < iters and err > abs_err:
        new = (current + value / current) / 2
        err = abs(current ** 2 - value)
        current = new
        count += 1

    return current


def main():
    try:
        user_input = input("Enter positive number: ")
    except EOFError:
        print("Never mind")
        return

    try:
        x = float(user_input)
    except ValueError:
        print("Input error: not number entered")
        return

    if x < 0:
        print("Input error: positive number required")
        return

    res = square_root(x)
    print(f"sqrt({x}) = {res}")


if __name__ == "__main__":
    main()
