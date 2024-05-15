def main():
    student_details = get_student_details()
    print(f"{student_details['name']} from {student_details['house']}")


def get_student_details():
    student_details = {"name": input("name: "), "house": input("house: ")}
    return student_details


if __name__ == "__main__":
    main()
