n = int(input())
for _ in range(n):

        s = input()
        res = ''
        for i in s:
            if i.islower():
                res += i
        print(res[::-1])
