
n = 1
while n != 0:
    n = int(input())
    for i in range(n):
        c = int(input())
        if c == 0:
            break
        if c % 2 == 0:
            print(c+(c-2))
        else:
            print(c+(c-1))
