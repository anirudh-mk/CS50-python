email = input("Enter your email id ").strip()

username, domain = email.split('@')
if username and domain.endswith(".com"):
    print("valid")
else:
    print("invalid")
