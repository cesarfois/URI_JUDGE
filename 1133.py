x = int(input())
y = int(input())

t = x
if x > y:
    x = y
    y = t

for x in range(x + 1 , y , 1):
    if x % 5 == 2 or x % 5 == 3:
        print(x)
