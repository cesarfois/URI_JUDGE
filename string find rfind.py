s = 'arara azul '

#primeira letra
print(s.find('a'))

#ultima letra
print(s.rfind('a'))

#frase
print(s.find('azu'))

#frase no achada retorna -1
print(s.find('auz'))

'''
The find() method returns an integer value.

    If substring exists inside the string, it returns the index of first occurence of the substring.
    If substring doesn't exist inside the string, it returns -1.

'''


