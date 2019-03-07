
'''
Yes, remove removes the first matching value, not a specific index:

>>> a = [0, 2, 3, 2]
>>> a.remove(2)
>>> a
[0, 3, 2]

del removes the item at a specific index:

>>> a = [3, 2, 2, 1]
>>> del a[1]
>>> a
[3, 2, 1]

and pop removes the item at a specific index and returns it.

>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]

while val_remove in my_list:
    my_list.remove(val_remove)

'''