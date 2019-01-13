def int_to_roman(input):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []

    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

n = int(input())

n = int_to_roman(n)

print(n)