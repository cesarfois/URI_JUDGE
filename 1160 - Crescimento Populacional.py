n = int(input())

for e in range(n):
    val = input().split()
    pa = int(val[0])
    pb = int(val[1])
    ca = float(val[2])
    cb = float(val[3])

    anos = 0
    while pb >= pa:
        cpa = int((pa * ca)/100)
        cpb = int((pb * cb)/100)

        anos = anos + 1
        pa = pa + cpa
        pb = pb + cpb


        if anos > 100:
            break

    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print('%d anos.' % anos)