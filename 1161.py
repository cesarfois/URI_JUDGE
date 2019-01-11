
while True:
    try:
        n, m = map(int, input().split())
        if n == 0:
            sum = 1
        else:
            sum = 1
            for i in range(1, n):
                sum = sum * (i + 1)

        if m == 0:
            sum1 = 1
        else:
            sum1 = 1
            for e in range(1, m):
                sum1 = sum1 * (e + 1)

        print(sum + sum1)

    except EOFError:
        break