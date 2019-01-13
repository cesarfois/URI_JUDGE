import math

while True:

        l = list(map(int,input().split()))
        if l[0] == 0:
            break

        areatot = l[0]*l[1]

        totalpermitido = (areatot * 100)/l[2]

        ladodoterreno = math.sqrt(totalpermitido)

        print('%d' %ladodoterreno)