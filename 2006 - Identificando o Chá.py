r = int(input())

l = list(map(int,(input().split())))
c = 0
for i in l:
    if i == r:
        c += 1

print(c)
