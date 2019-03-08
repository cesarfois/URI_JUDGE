'''
from collections import deque
>>> d=deque([1,2,3,4,5])
>>> d
deque([1, 2, 3, 4, 5])
>>> d.rotate(2)
>>> d
deque([4, 5, 1, 2, 3])
>>> d.rotate(-2)
>>> d
deque([1, 2, 3, 4, 5])

Or with list slices:

>>> li=[1,2,3,4,5]
>>> li[2:]+li[:2]
[3, 4, 5, 1, 2]
>>> li[-2:]+li[:-2]
[4, 5, 1, 2, 3]

Note that the sign convention is opposite with deque.rotate vs slices.

If you want a function that has the same sign convention:

def rotate(l, y=1):
   if len(l) == 0:
      return l
   y = -y % len(l)     # flip rotation direction
   return l[y:] + l[:y]

>>> rotate([1,2,3,4,5],2)
[4, 5, 1, 2, 3]
>>> rotate([1,2,3,4,5],-22)
[3, 4, 5, 1, 2]
>>> rotate('abcdefg',3)
'efgabcd'

For numpy, just use np.roll

>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.roll(a, 1)
array([9, 0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> np.roll(a, -1)
array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

'''