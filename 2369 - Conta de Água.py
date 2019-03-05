n = int(input())
res = 0
if n <= 10:
    res = 7
else:
    if 10 < n <= 30:
        res = (n - 10) * 1 + 7
    elif 30 < n <= 100:
        res = (n - 30) * 2 + 27
    elif n > 100:
        res = (n - 100) * 5 + 167

print(res)




