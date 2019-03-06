for i in range(int(input())):
    p = int(input())
    print(' '.join(sorted(list(map(str, input().split())), key=int)))
