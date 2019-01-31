n = int(input())

for _ in range(n):

        n1 = int(input())
        l = list(map(int, input().split()))
        l1 = l.copy()
        c = 0
        l = sorted(l, reverse=True)

        for i in range(len(l)):
            if l[i] != l1[i]:
                c += 1
        print(len(l) - c)
