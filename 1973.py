n = int(input())

lista = list(map(int,input().split()))
sum = 0
for i in lista:
    i = i - 1
    sum = sum + i

print(sum)
