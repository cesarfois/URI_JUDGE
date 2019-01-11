n = int(input())

for i in range(n):
    s = input()
    a = (len(s)/2)

    s1 = s[:int(a)]
    s2 = s[int(a):]
    s1 = s1[::-1]
    s2 = s2[::-1]

    print(s1+s2)