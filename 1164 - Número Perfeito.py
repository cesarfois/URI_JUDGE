qde = int(input())
for e in range(qde):
    n = int(input())
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if n == sum:
        print('%d eh perfeito' % n)
    else:
        print('%d nao eh perfeito' % n)