t = int(input())
for _ in range(t):
    l =[]
    n = int(input())
    for i in range(n):
        s = input()
        if s == 'LEFT':
            l.append(-1)
        elif s == 'RIGHT':
            l.append(1)
        elif s[:7] == 'SAME AS':
            l.append(l[int(s[8:])-1])
    print(sum(l))