while True:
    vet = [str(x) for x in input().split()]
    a = vet[0]
    b = vet[1]
    if a == '0' and b == '0':
        break
    a = '0'*(9-len(a)) + a
    b = '0'*(9-len(b)) + b
    carry = count = 0
    i = 8
    while i >= 0:
        if int(a[i]) + int(b[i]) + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        i -= 1
    if carry == 1:
        count += 1
    if count == 0:
        print('No carry operation.')
    elif count == 1:
        print('1 carry operation.')
    else:
        print(str(count) + ' carry operations.')