# Python program to right rotate a list by n

# Returns the rotated list
def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list


# Driver Code Another approach to solve this problem by using slicing technique. One way of slicing list is by using len() method.
rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]

print(rightRotate(list_1, rotate_num))
# Python program to right rotate
# a list by n using list slicing
n = 3

list_1 = [1, 2, 3, 4, 5, 6]
list_1 = (list_1[len(list_1) - n:len(list_1)]
				+ list_1[0:len(list_1) - n])
print(list_1)

# Right Rotating a list to n positions n the above method, last n elements of list_1 was taken and then remaining elements of list_1. Another way is without using len() method
n = 3

list_1 = [1, 2, 3, 4, 5, 6]
list_1 = (list_1[-n:] + list_1[:-n])

print(list_1)
