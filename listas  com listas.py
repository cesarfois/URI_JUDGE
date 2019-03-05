dadosl = ['pedro', 25]
dadosl1 = ['Maria', 18]

pessoasl =[]

# inserir uma lista dentro de outra lista
# cuidado utilizar [:] para fazer copia
pessoasl.append(dadosl[:])
pessoasl.append(dadosl1[:])

# Declarar uma lista

pessoas2 = [['pedro', 25], ['Maria', 18]]

# Selecionando a idade de pedro.

print(pessoas2[0][1])

# trazer todos os elementos do iten 0
print(pessoas2[0])

# Adicionando elementos
for c in range(3):
    dadosl.append(str(input('Nome: ')))
    dadosl.append(int(input('Idade: ')))
    pessoas2.append(dadosl[:])
    dadosl.clear()

for p in pessoas2:
    if p[1] >= 21:
        print(p[0])

print(pessoas2)


print(pessoasl)

