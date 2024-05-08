name = input("Enter your name: ")

match name:
    case "Hary" | "Harmony" | "Ron":
        print("Gryffindor")
    case "man":
        print("usa")
    case "girl":
        print("uk")
    case _:
        print("joan")
