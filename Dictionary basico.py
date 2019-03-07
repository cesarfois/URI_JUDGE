print()

dados = {'nome':'Pedro', 'idade': 25}

# Criando um elemento
dados['sexo'] = 'M'

# Removendo um elemento e o valor dele
#del dados['idade']

# imprimindo somente as chaves
print(dados.keys(), 'imprimindo somente as chaves\n')

# imprimindo somente os valores
print(dados.values(),'imprimindo somente os valores\n')

# imprimindo todos os itens
print(dados.items(),'imprimindo todos os itens\n')

print(dados)