n = int(input())

for i in range(n):

        val = input().split()
        x = float(val[0])
        y = float(val[1])
        if y == 0:
            print('divisao impossivel')
        else:
            print('%.1f' % (x/y))
