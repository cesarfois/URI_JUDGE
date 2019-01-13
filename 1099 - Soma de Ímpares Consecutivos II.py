n = int(input())
a, sum = 0, 0
for i in range(n):
    val = input().split()
    x = int(val[0])
    y = int(val[1])
    if x <= y:
        for a in range(x+1, y, 1):
            if a % 2 != 0:
                sum = sum + a
        print(sum)
    else:
        for a in range(y + 1, x, 1):
            if a % 2 != 0:
                sum = sum + a
        print(sum)
    sum = 0


