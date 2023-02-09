def powerOf2(n):
    mul = 1
    print(mul*2)
    while(mul < n):
        mul = (mul*2)

    return True if mul == n else False


print(powerOf2(225))
