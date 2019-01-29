prop = cpf = ''
s = input()
s1 = input()
a = b = c = d = ''
flag = flag1 = False
for i in s:
    if i.isdigit():
        cpf += i
    elif i == str('.') and flag is False:
        cpf += i
        flag = True

for e in s1:
    if e.isdigit():
        prop += e
    elif e == str('.') and flag1 is False:
        prop += e
        flag1 = True

if str('.') in s:
    a, b = str(cpf[11:]).split('.')
    a = ''.join(str(a) + str('.') + str(b[:2]))
else:
    a = str(cpf[11:])
if str('.') in s1:
    c, d = prop.split('.', 1)
    c = ''.join(str(c) + str('.') + str(d[:2]))
else:
    c = str(prop)

print('cpf %s' % str(cpf[:11]))
print('%.2f' % (float(a) + float(c)))
