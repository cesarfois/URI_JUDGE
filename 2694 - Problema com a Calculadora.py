import re

n = int(input())
for w in range(n):
        s = input()
        s1 = ''
        l = []
        for i in s:
            if re.match('[a-zA-Z]', i):
                s1 += ' '
            else:
                s1 += i

        l = s1.split()
        a = sum(map(int, l))
        print(a)