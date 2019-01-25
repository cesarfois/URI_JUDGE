s = input()
s1 = input()

c = 0
max = 0
subs = ''
for i in range(len(s)):
    for j in range(len(s1)):
        if s[i] == s1[j]:
                n = int(i)
                m = int(j)
                while n < len(s1):
                    if s[n] == s1[m]:
                        c += 1
                    m += 1
                    n += 1

print(max,c)

