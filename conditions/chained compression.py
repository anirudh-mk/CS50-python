score = int(input("Enter your score: "))

if 90 <= score <= 100:  # chained compression
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
elif 50 <= score < 60:
    print("Grade E")
else:
    print("Failed")
