import re
n = int(input())

for i in range(n):
    s = input()
    if len(s) == 8:
        if s[3] == '-' and re.match("[A-Z]", s[:3]) and re.match("[0-9]", s[4:]):
            if s[-1] == '1' or s[-1] == '2':
                print('MONDAY')
            elif s[-1] == '3' or s[-1] == '4':
                print('TUESDAY')
            elif s[-1] == '5' or s[-1] == '6':
                print('WEDNESDAY')
            elif s[-1] == '7' or s[-1] == '8':
                print('THURSDAY')
            elif s[-1] == '9' or s[-1] == '0':
                print('FRIDAY')
        else:
            print('FAILURE')
    else:
        print('FAILURE')