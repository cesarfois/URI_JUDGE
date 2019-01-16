
while True:
    try:
        t, v = map(int, input().split())

        res = v * (t*2)

        print(res)
    except EOFError:
        break

