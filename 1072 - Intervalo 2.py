n = int(input())
dentro, fora = 0, 0


for x in range(n):
    a = float(input())

    if int(a) in range(10, 20):
        dentro = dentro + 1
    else:
        fora = fora + 1

print("%d in" % dentro)
print("%d out" % fora)
