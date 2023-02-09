def plusOne(digits):

    # for i in range(-1, len(digits), -1):
    length = len(digits)

    # if length == 1 and digits[0] == 9:
    #     return [1, 0]

    for i in range(-1, -(length + 1), -1):
        print(i)
        if digits[i] == 9:
            digits[i] = 0
            if i == -(length):
                digits.insert(0, 1)
        else:
            digits[i] = digits[i]+1
            return digits

    return digits


print(plusOne([1, 2, 3]))
print(plusOne([1, 9, 9]))
