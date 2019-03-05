ni = int(input())

for _ in range(ni):
        n = int(input())
        res = 0
        for e in range(n):
            s = input()
            for i in range(len(s)):
                res = res + (ord(s[i]) - 65) + e + i
        print(res)