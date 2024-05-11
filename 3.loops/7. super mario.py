def main():
    print_column(3)
    print_square(3)


def print_column(columns):
    for _ in range(columns):
        print("#")


def print_square(n):
    for _ in range(n):
        print("#"*n)


main()
