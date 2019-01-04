
n = int(input())
c = 1

for x in range(1,(n*2)+1,1):
   if x % 2 == 0:
      print(c, (c**2)+1, (c**3)+1)
      c += 1
   else:
      print(c, (c ** 2), (c ** 3))
