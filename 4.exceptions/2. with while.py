while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
        print("x is not integer")
    else:
        break
print(f"value of x is {x}")