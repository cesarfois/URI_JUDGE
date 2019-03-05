import re

n = int(input())

for i in range(n):
    l = input()
    b = l[1]

    if int(l[2]) == int(l[0]):
        res = int(l[2]) * int(l[0])
    elif re.match("[A-Z]", b):
        res = int(l[2]) - int(l[0])
    elif re.match("[a-z]", b):
        res = int(l[2]) + int(l[0])

    print(res)