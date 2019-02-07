from _datetime import datetime
z = '22/12/2012  '
#convertendo para formato date
f = datetime.strptime(z, '%d/%m/%Y')

#imprimindo num formato

print(f.strftime('%d/%m/%Y'))

# https://blog.alura.com.br/lidando-com-datas-e-horarios-no-python/

#imprimindo sem zeros na frente
print(l2[0].strftime('%#d/%#m/%Y'))

time.strftime('%Y %m %d', y).replace(' 0', ' ')