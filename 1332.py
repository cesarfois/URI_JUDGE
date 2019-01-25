
n = int(input())
for i in range(n):
        s = input()
        c = 0
        if len(s) > 3:
            print('3')
        else:
            if s[0] == 'o':
                c += 1
            if s[1] == 'n':
                c += 1
            if s[2] == 'e':
                c += 1
            if c >= 2:
                print('1')
            else:
                print('2')


