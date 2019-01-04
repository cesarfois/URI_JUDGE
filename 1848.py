som = 0
c = 1
while c <= 3:
    try:
        n = str(input())

        if n == "--*":
            som = som + 1
        elif n == "-*-":
            som = som + 2
        elif n == "---":
            som = som
        elif n == "-**":
            som = som + 3
        elif n == "*--":
            som = som + 4
        elif n == "*-*":
            som = som + 5
        elif n == "**-":
            som = som + 6
        elif n == "***":
            som = som + 7
        elif n == 'caw caw':
                print(som)
                som = 0
                c += 1
    except:
        break
