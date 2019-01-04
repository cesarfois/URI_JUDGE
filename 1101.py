val = input().split()

sum, n, m = 0, 0, 0
n = int(val[0])
m = int(val[1])

if n > 0 and m > 0:

    if n <= m and (n != 0) and (m != 0):
        for x in range(n, m + 1, 1):
            sum = sum + x
            print(x, end=' ')
        print('Sum=%d' % sum)


    if n > m and (n != 0) and (m != 0):
        for x in range(m, n + 1, 1):
            sum = sum + x
            print(x, end=' ')
        print('Sum=%d' % sum)

print("\n")