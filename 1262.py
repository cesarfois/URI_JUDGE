NAO COMPLETADO


s = input()

st = True

print(s)
p = 4
res = 1
clock = 1
for i in s:
    if clock <= p:
        if i == 'W':
            res += 1
            clock += 1
        elif i == 'R' and clock == p:
            res += 1
            clock = 1
        elif i == 'R' and s[i+1:] == 'W':
            res += 1
        else:
            clock += 1




print(res)