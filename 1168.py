
num = {'0': 6,
       '1': 2,
       '2': 5,
       '3': 5,
       '4': 4,
       '5': 5,
       '6': 6,
       '7': 3,
       '8': 7,
       '9': 6}

n = int(input())
for i in range(n):
    l = input()
    l = list(l)
    sum = 0
    for e in l:
        sum += num[e]
    print('%d leds' % sum)
