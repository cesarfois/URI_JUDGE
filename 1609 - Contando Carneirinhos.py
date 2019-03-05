n = int(input())
for i in range(n):
    no = int(input())
    l = list(map(int,input().split()))
    l = set(l)
    print(len(l))