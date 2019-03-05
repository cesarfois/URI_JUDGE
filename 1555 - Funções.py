n = int(input())

for i in range(n):
        x, y = map(int,input().split())

        rafa = (((3*x)*(3*x)) + (y*y))/x*y
        beto = ((2*(x*x)) + ((5*y)*(5*y)))/x*y
        carlos = ((-100*x) + (y*y*y))/x*y

        if rafa > beto and rafa > carlos:
            print('Rafael ganhou')
        elif beto > rafa and beto > carlos:
            print('Beto ganhou')
        elif carlos > rafa and carlos > beto:
            print('Carlos ganhou')