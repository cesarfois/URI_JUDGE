while True:
    try:
        val = input().split()
        x = int(val[0])
        y = int(val[1])
        if x == 0 or y == 0:
            break
        if x > 0 and y > 0:
            print('primeiro')
        if x < 0 and y < 0:
            print('terceiro')
        if x > 0 and y < 0:
            print('quarto')
        if x < 0 and y > 0:
            print('segundo')
    except:
        break
