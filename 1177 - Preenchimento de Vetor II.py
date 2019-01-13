
n = int(input())

temp = 0

for i in range(1000):
    print("N[%d] = %d" % (i, temp))
    temp = temp + 1
    if n == temp:
        temp = 0