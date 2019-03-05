d = int(input())

a, b, c = map(int,input().split())

if a >= d and b >= d and c >= d:
    print('S')
else:
    print('N')