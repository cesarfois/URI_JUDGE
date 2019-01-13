
while True:
    try:
        n = int(input())
        if n == -1:
            break

        if n == 0:
            print('0')
        else:
            print(n - 1)
    except EOFError:
        break
