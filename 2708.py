c = res = 0
while True:
    try:
        s = input()
        if s == "ABEND":
            print(res)
            print(c)
            break
        a, b = s.split()
        if a == "SALIDA":
            c += 1
            res += int(b)
        elif a == "VUELTA":
            c -= 1
            res -= int(b)

    except EOFError:
        break