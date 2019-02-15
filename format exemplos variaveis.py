'''

print '{0:>{x}}'.format('foo', x=x)

print '{:<}{:>20}.format(a,b)'
       foo


n = 9
for e in range(1,10,2):
    print('{0:^{x}}'.format('*'*e, x=n))

    print('Ent{0}o é N{0}t{0}l!'.format('a'*n))


    print('Ent{0}o é N{0}t{0}l!'.format('a'*n,x=n))
    print('Ent{}o é N{}t{}l!'.format('a'*n,'a'*n,'a'*n, n))

 print('k'+'a'*(c*m))

https://pyformat.info/

a  = 1
b = 2
c = 3
print('A = %d, B = %d, C = %d' %(a,b,c))
print('A = {:>10}, B = {:>10}, C = {:>10}'.format(a, b, c))
print('A = {:>10}, B = {:>10}, C = {:>10}'.format(str(a).zfill(10), str(b).zfill(10), str(c).zfill(10)))
print('A = {:<10}, B = {:<10}, C = {:<10}'.format(a, b, c))



'''

lanche = ['hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita']

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('Comi pra caramba!')

print('='*72)
print('{0:=^72}'.format(' Exercicio 5.11 '))
print('{0:=^72}'.format(' By César J. Fois '))
print('='*72)
print('{0:=^72}'.format(' Mostrar taxas 24 Meses '))
print('='*72)
print('')

print('-'*39)
print('|{:<37}|'.format('x = 35'))
print('|'+' '*37 + '|')
print('|{:^37}|'.format('x = 35'))
print('|'+' '*37 + '|')
print('|{:>37}|'.format('x = 35'))
print('-'*39)

print('-'*39)
print('| {:^10}|{:^9}|{:^15}|'.format('decimal','octal','Hexadecimal'))
print('-'*39)
for i in range(16):
    print('|  {:^9}|{:^9o}|{:^15X}|'.format(i,i,i))
print('-'*39)

