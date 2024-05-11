def main():
    x = int(input("What is x: "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # or

    # return True if num % 2 == 0 else False

    # or

    return num % 2 == 0


main()
