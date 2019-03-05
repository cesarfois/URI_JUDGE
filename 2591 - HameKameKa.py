
n = int(input())
for _ in range(n):
        a, b = map(str,input().split('k'))
        c = m = 0
        for i in a:
            if i == 'a':
                c += 1

        for e in b:
            if e == 'a':
                m += 1
        print('k'+'a'*(c*m))