def mdc(a, b):
    return a if not b else mdc(b, a % b)

t = int(input())

for x in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    print(mdc(a, b))