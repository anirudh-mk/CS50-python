def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("enter your name: ")
    house = input("enter your house")
    return (name, house)


if __name__ == "__main__":
    main()
