i = 0
j = 1
for x in range(3):
    print("I=%d J=%d" % (i, j))
    j = j + 1

for x in range(9):
    j = j - 3
    j = j + 0.2
    i = i + 0.2
    for x in range(3):
        if (i == 1):
            print("I=%d J=%d" % (i, j))
        else:
            print("I=%.1f J=%.1f" % (i, j))
        j = j + 1

i = 2
j = 3
for x in range(3):
    print("I=%d J=%d" % (i, j))
    j = j + 1



