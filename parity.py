def main():
    x = int(input("What's x?\n"))
    if is_even(x):
        print(f"{x} is an even number.")
    else:
        print(f"{x} is an odd number")


def is_even(n):
    return n % 2 == 0

    # return True if n % 2 == 0 else False

    # if n % 2 == 0:
    #     return True
    # else:
    #     return False


main()
