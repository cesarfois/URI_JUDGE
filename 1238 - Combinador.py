
n = int(input())

for i in range(n):
        s, s1 = map(str,input().split())
        res = ''

        if len(s) <= len(s1):
            for i in range(len(s)):
                res += s[i]
                res += s1[i]
            res += s1[len(s):]
        else:
            for i in range(len(s1)):
                res += s[i]
                res += s1[i]
            res += s[len(s1):]

        print(res)

