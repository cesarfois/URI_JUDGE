diai = input().split()
tempoi = input().split(' : ')
diaf = input().split()
tempof = input().split(' : ')

di = int(diai[1])
df = int(diaf[1])
hi, mi, si = tempoi
hf, mf, sf = tempof

dt = df - di

ht = int(hf) - int(hi)
if ht < 0:
    ht = int(hf) + (24 - int(hi))
    dt = dt - 1

mt = int(mf) - int(mi)
if mt < 0:
    mt = int(mf) + (60 - int(mi))
    ht = ht - 1

st = int(sf) - int(si)
if st < 0:
    st = int(sf) + (60 - int(si))
    mt = mt - 1

if dt <= 0:
    dt = 0

print('%d dia(s)' % dt)
print('%d hora(s)' % ht)
print('%d minuto(s)' % mt)
print('%d segundo(s)' % st)