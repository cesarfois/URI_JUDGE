n = int(input())

l = list(map(int, input().split()))

i, anterior, res = 1,0,0

while i < n:
    if l[anterior] > l[i]:
        i += 1
        res = i
        break
    i += 1
    anterior += 1

print(res)