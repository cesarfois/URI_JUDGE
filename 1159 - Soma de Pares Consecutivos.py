

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 != 0:
        n = n + 1
    sum = 0
    for i in range(5):
        sum = sum + n
        n = n + 2
    print(sum)

