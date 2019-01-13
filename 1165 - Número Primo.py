qde = int(input())

for e in range(qde):
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum = sum + 1
    if sum > 2:
        print("%d nao eh primo" % n)
    else:
        print("%d eh primo" %n)