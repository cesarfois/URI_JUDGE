while True:
    try:

        td, ud, wd, cd = map(int,input().split())
        if ud*100/td >= cd:
            print('critical')
        elif ud*100/td >= wd:
            print('warning')
        else:
            print('OK')

    except EOFError:
        break
