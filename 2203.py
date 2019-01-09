
while True:
    try:
        x1, y1, x2, y2, vi, r1 , r2 = map(int,input().split())

        d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

        distotal = d + (vi * 1.5)

        rtotal = r1 + r2

        if distotal <= rtotal:
            print('Y')
        else:
            print('N')
    except EOFError:
        break