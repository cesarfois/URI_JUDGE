l=[]
t = int(input())
fc = int(input())

for f in range(fc):
    n = int(input())
    if n not in l:
        l.append(n)
        t -= 1
print(t)

