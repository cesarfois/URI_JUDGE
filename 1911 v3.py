#Wrong answer 10%
while True:
    try:
        orig = {}
        sala = {}
        res = 0
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            a, b = map(str,input().split())
            if len(a) > 20:
                break
            orig[a] = b
        n = int(input())
        for i in range(n):
            c, d = map(str,input().split())
            sala[c] = d

        for i in sala.keys():
            if len(set(sala[i]) - set(orig[i])) > 1 or len(set(orig[i]) - set(sala[i])) > 1:
                res += 1

        print(res)
    except EOFError:
        break