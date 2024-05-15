import re

email = input("Enter your email ")

if re.search(r"^\w+@\w+\.(com|edu|gov)$", email):
    print("Valid")
else:
    print("invalid")

"""
    [] set character
    [^] not set
    A|B a or b
    (..) a group
    (?..) non capturing version
    \d decimal digit
    \D not a decimal digit
    \s whitespace character
    \S not a whitespace character
    \w word character with numbers and underscore
    \W not a word character
    re.IGNORECASE ignore uppercase
    re.MULTILINE 
    re.
"""
