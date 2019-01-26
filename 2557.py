import re
while True:
    try:

        s = input()
        if s == '':
            break
        s1 = s.replace('+',',')
        s1 = s1.replace('=', ',')
        s1 = s1.split(',')

        res = 0
        if re.match('[A-Z]', s1[0]):
            s1[0] = s1[2]
            s = s.replace(s[1], '-')
            res = int(s1[0]) - int(s1[1])
        elif re.match('[A-Z]', s1[1]):
            s1[1] = s1[2]
            s = s.replace(s[1], '-')
            res = int(s1[1]) - int(s1[0])
        else:
            res = int(s1[0]) + int(s1[1])

        print(res)
    except EOFError:
        break