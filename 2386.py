l = int(input())
n = int(input())
res = 0
for i in range(n):
    a = int(input())
    if a * l >= 40000000:
        res += 1

print(res)
