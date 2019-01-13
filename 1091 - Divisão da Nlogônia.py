

while True:
    try:
        t = int(input())
        if t == 0:
            break
        n, m = map(int, input().split())

        for i in range(t):
            x, y = map(int,input().split())

            if (n == x) or (m == y):
                print("divisa")
            else:
                if x > n and y > m:
                    print("NE")
                if x > n and y < m:
                    print("SE")
                if x < n and y > m:
                    print("NO")
                if x < n and y < m:
                    print("SO")

    except EOFError:
        break