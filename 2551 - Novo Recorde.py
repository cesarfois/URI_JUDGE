while True:
    try:

        n = int(input())
        res = 0
        c = 0
        for i in range(1,n+1):
            a,b = map(int,input().split())
            if res < b/a:
                res = b/a
                print(i)
    except EOFError:
        break