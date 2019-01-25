n1 = int(input())
for i in range(n1):

        l = []

        n = int(input())
        for i in range(n):
            l.append(input())

        a = all(x == l[0] for x in l)

        if a is False:
            print('ingles')
        else:
            print('%s' % l[0])
