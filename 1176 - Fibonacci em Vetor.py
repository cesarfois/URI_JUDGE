n = int(input())
lista = [0,1]
i, t1 = 0, 0
t2 = 1
for e in range(n):
    f = int(input())
    while i < 60:
        t3 = t1 + t2
        lista.append(t3)
        t1 = t2
        t2 = t3
        i += 1
    print("Fib(%d) = %d" % (f, lista[f]))

