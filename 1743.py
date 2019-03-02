m = list(map(int,input().split()))
f = list(map(int,input().split()))
aux = []
for i in m:
    if i == 1:
        aux.append(0)
    else:
        aux.append(1)
if f == aux:
    print('Y')
else:
    print('N')