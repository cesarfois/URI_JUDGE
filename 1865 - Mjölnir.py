n = int(input())

for i in range(n):
    r, v = map(str, input().split())
    if r == 'Thor':
        print('Y')
    else:
        print('N')
