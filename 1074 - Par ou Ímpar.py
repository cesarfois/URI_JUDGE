n = int(input())

for x in range(n):
    a = int(input())
    if a == 0:
        print("NULL")
    if a > 0 and a % 2 == 0:
        print("EVEN POSITIVE")
    elif a < 0 and a % 2 == 0:
        print("EVEN NEGATIVE")
    elif a > 0 and a % 2 != 0:
        print("ODD POSITIVE")
    elif a < 0 and a % 2 != 0:
        print("ODD NEGATIVE")

