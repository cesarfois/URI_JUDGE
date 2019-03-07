from datetime import datetime

Ano_Nascimento = int(input())

idade = datetime.now().year - Ano_Nascimento

print(idade)