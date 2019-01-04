p, n = map(int, input().split())

l = list(map(int, input().split()))
res = ''
for i in range(1,n):
    if abs((l[i-1] - l[i])) > p:
        res = "PERDEU"

if res == 'PERDEU':
    print('GAME OVER')
else:
    print('YOU WIN')