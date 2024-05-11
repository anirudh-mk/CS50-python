try:
    x = int(input("what is x: "))
    y = int(input("what is y: "))
except ValueError:
    print("enter valid number")
else:
    if x > y:
        print("x is large")
    elif x < y:
        print("y is large")
    else:
        print("x equals y")
