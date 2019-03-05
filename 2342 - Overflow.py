n = int(input())

a, o, b = map(str,input().split())
res = 0
if o == '*':
    res = int(a) * int(b)
elif o == '+':
    res = int(a) + int(b)

if res > n:
    print('OVERFLOW')
else:
    print('OK')