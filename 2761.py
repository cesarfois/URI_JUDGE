l = list(map(str, input().split()))
s = ''
a = int(l[0])
b = float(l[1])
c = str(l[2])
for i in range(3, len(l)):
    s += l[i] + ' '
d = s.rstrip()

print('{}{}{}{}'.format(a, b, c, d))
print('{}\t{}\t{}\t{}'.format(a, b, c, d))
print('{:>10}{:>10}{:>10}{:>10}'.format(a, b, c, d))