n = int(input())

for i in range(n):
    s = ''
    l = list(map(str,input().split()))
    l.sort(key=len,reverse=True)
    for i in l:
        s = s + i + ' '
    print(s[:-1])
