cv, ce, cs, fv, fe , fs = map(int, input().split())

tc = (cv*3) + ce
tf = (fv*3) + fe

if tc > tf:
    print('C')
elif tc < tf:
    print('F')
elif tc == tf and fs == cs:
    print('=')
elif tc == tf and fs > cs:
    print('F')
elif tc == tf and fs < cs:
    print('C')