import sys

# python filename.py {Argv}
# python 5.librarys\5.sys.py anirudh

try:
    print("hello", sys.argv[1])     # print hello anirudh
except IndexError:
    print("hello")