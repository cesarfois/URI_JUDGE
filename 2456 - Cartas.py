l = list(map(int, input().split()))
if sorted(l) == l:
    print("C")
elif sorted(l, reverse=True) == l:
    print('D')
else:
    print('N')