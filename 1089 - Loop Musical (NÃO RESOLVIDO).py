
#n = int(input())

l = list(map(int,input().split()))
l1 = [0]
c = 1
res,temp = 0, 0
pico = 'N'

while c < (len(l)):
    temp = l[c]
    for i in l:
        print(i, temp)
        if i > temp:
            pico = 'N'
        else:
            pico = 'P'
        if i > temp and pico == 'P':
            res += 1
        if i < temp and pico == "N":
            res += 1
    c += 1
print(res)

