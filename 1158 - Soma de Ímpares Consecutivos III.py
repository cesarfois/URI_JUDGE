
n = int(input())

for i in range(1, n+1):
    val = input().split()
    x = int(val[0])
    if x % 2 == 0:
        x= x + 1
    y = int(val[1])

    sum = 0
    for e in range(y):
        sum = sum + x
        x = x + 2
    print(sum)
