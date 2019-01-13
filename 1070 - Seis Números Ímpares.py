a = int(input())
b = int(input())
res = 0

if a < b:
    for x in range((a+1), b, 1):
        if x % 2 != 0:
            res = res + x
if a > b:
    for x in range((b+1), a, 1):
        if x % 2 != 0:
            res = res + x

print(res)