print('-'*39)
print('| {:^10}|{:^9}|{:^15}|'.format('decimal','octal','Hexadecimal'))
print('-'*39)
for i in range(16):
    print('|  {:^9}|{:^9o}|{:^15X}|'.format(i,i,i))
print('-'*39)

