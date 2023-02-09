def addBinary(a, b):
    if len(a) > len(b):
        b = '0'*(len(a)-len(b)) + b

    if len(b) > len(a):
        a = '0'*(len(b)-len(a)) + a

    carry = 0

    result = ''

    for i in range(len(a)-1, -1, -1):
        sum = int(a[i]) + int(b[i]) + carry
        if sum == 3:
            result = '1' + result
            carry = 1
        elif sum == 2:
            result = '0' + result
            carry = 1
        elif sum == 1:
            result = '1' + result
            carry = 0
        else:
            result = '0' + result
            carry = 0

    if carry == 1:
        result = '1' + result

    return result


print(addBinary("11", "1"))
