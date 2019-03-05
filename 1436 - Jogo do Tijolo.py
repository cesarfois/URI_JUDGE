n = int(input())

for i in range(1, n+1):
        l = list(map(int,input().split()))
        a = int(len(l)/2)
        if len(l) % 2 == 0:
            print('Case %d: %d' %(i, l[a]))
        else:
            print('Case %d: %d' %(i, l[a+1]))