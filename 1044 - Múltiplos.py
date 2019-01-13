
string = input().split()

a = int(string[0])
b = int(string[1])

if b % a == 0 or a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

