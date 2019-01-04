n = int(input())

lista = list(map(int,input().split()))
sum = 0
for i in lista:
    i = i - 1
    sum = sum + i

print(sum)

1 3 5 7 11 13 16 19
      2 4 6 10 12 15 18