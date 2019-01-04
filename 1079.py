n = int(input())

for x in range(n):
    val = input().split()
    sum = ((float(val[0]) * 2)+(float(val[1]) * 3)+(float(val[2]) * 5))/10
    print('%.1f' % sum)
