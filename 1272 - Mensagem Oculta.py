n = int(input())

for i in range(n):
    l = list(map(str, input().split()))
    for i in range(len(l)):
        print(l[i][0], end='')
    print()