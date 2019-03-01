while True:
    try:
        n = int(input())
        if n == 0:
            break

        l = list(map(int, input().split()))

        m = l.count(0)
        j = l.count(1)

        print('Mary won %d times and John won %d times' % (m, j))

    except EOFError:
        break
