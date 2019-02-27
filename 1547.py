nn = int(input())
for e in range(nn):

        a, e = map(int,input().split())
        l = list(map(int,input().split()))
        l1 = []
        menor = 100
        for i in range(len(l)):
            if l[i] == e:
                l1.append(i+1)
                break
            elif abs(l[i] - e) < menor:
                menor = abs(l[i] - e)
                l1.append(i + 1)
        print(l1[-1])