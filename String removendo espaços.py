texto = ('Willian    ','Silva         ','  Guj           ')
texto2 = []
for i in texto:
    texto2.append(''.join(i.split(' ')))
print(texto2)
#resultado: ['Willian', 'Silva', 'Guj'']