for _ in range(int(input())):

    s = input().lower()
    res = ""
    l = [0]
    for letra in s:
        if letra.isalpha():
            if s.count(letra) >= max(l):
                l.append(s.count(letra))

    for letra in s:
        if s.count(letra) == max(l):
            if not letra in res:
                res += letra
    print(''.join(sorted(res)).strip())