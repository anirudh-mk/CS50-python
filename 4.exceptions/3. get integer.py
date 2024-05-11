def main():
    x = get_int("what is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not a integer enter an valid integer")

main()