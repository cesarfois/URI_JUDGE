a,b,c = map(int, input().split())
x,y,z = map(int, input().split())

if a > x or b > y or c > z:
    res = 0
else:
    res = (int(x/a) * int(y/b)) * int(z/c)

print(res)