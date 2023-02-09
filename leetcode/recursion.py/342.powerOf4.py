def powerOf4(n):
    mul = 1
    print(mul*4)
    while(mul < n):
        mul = (mul*2)

    return True if mul == n else False


print(powerOf4(17))
