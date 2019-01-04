n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    c = 0
    if a == 1001:
        c = b * 1.50
        sum = sum + c

    elif a == 1002:
        c = b * 2.50
        sum = sum + c
    elif a == 1003:
        c = b * 3.50
        sum = sum + c
    if a == 1004:
        c = b * 4.50
        sum = sum + c
    elif a == 1005:
        c = b * 5.50
        sum = sum + c

print('%.2f' % sum)