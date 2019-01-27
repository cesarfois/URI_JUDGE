n = int(input())

for e in range(n):
        s = input()
        res = ''
        f = 0
        for i in range(len(s)):
            if s[:2] == "RA" and len(s) == 20 and s[3:].isdigit():
                if s[i].isdigit() and s[i] != '0':
                    f = int(i)
                    print(s[f:])
                    break
            else:
                print('INVALID DATA')
                break