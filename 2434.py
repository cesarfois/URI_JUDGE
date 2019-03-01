n, si = map(int, input().split())
l = []
l.append(si)
for i in range(n):
    a = int(input())
    res = l[-1] + a
    l.append(res)

print(min(l))