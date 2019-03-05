n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    print('%d cm2' %((a*b)/2))
