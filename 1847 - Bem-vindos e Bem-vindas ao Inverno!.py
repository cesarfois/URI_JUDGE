

a, b, c = map(int, input().split())


if a > b and b <= c:
    print(':)')
elif a < b and b >= c:
    print(':(')
elif a < b and b < c and (b - a) > (c - b):
    print(':(')
elif a < b and b < c and (b - a) <= (c - b):
    print(':)')
elif a > b and b > c and (a - b) > (b - c):
    print(':)')
elif a > b and b > c and (a - b) <= (b - c):
    print(':(')
elif a == b and b > c:
    print(':(')
elif a == b and b < c:
    print(':)')
else:
    print(':(')



