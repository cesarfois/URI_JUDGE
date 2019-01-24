
n = int(input())

for _ in range(n):
    s = input()
    c = int(input())
    res = ''
    for i in s:
        if ord(i) >= (65 + c):
            res += chr(ord(i) - c)
        else:
            res += chr((ord(i) - c) + 26)

    print(res)