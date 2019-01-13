x = input().split()
hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])
if(hi == hf) & (mi == mf):
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
  ht = hf - hi
  mt = mf - mi
  if(ht < 0):
    ht += 24
  if(mt < 0):
    mt += 60
    ht -= 1
  print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(ht, mt))