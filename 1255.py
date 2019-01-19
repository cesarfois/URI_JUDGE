s = input()
s1 = input()
s = s.replace(' ','')
s1 = s1.replace(' ','')
c = 0

for i in s:
    if i in s1:
        print(i)
        c += 1

print(c)