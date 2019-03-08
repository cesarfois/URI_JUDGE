n = int(input())
for i in range(n):
        s = input()
        res = ''
        for i in s:
            if i != ' ':
                if i == 'G' or i == 'Q' or i == 'a' or i == 'k' or i == 'u':
                    res += '0'
                elif i == 'I' or i == 'S' or i == 'b' or i == 'l' or i == 'v':
                    res += '1'
                elif i == 'E' or i == 'O' or i == 'Y' or i == 'c' or i == 'm' or i == 'w':
                    res += '2'
                elif i == 'F' or i == 'P' or i == 'Z' or i == 'd' or i == 'n' or i == 'x':
                    res += '3'
                elif i == 'J' or i == 'T' or i == 'e' or i == 'o' or i == 'y':
                    res += '4'
                elif i == 'D' or i == 'N' or i == 'X' or i == 'f' or i == 'p' or i == 'z':
                    res += '5'
                elif i == 'A' or i == 'K' or i == 'U' or i == 'g' or i == 'q':
                    res += '6'
                elif i == 'C' or i == 'M' or i == 'W' or i == 'h' or i == 'r':
                    res += '7'
                elif i == 'B' or i == 'L' or i == 'V' or i == 'i' or i == 's':
                    res += '8'
                elif i == 'H' or i == 'R' or i == 'j' or i == 't':
                    res += '9'

        print(res[:12])