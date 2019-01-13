x = int(input())
y = int(input())
t13, sum = 0, 0

t = x
if x > y:
    x = y
    y = t

for x in range(x , y + 1 , 1):
    sum = sum + x
    if x % 13 == 0:
        t13 = t13 + x
print(sum - t13)