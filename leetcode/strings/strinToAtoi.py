
def myAtoi(s):
    sign = "+"

    pointBeforDigit = []
    pointAfterDigit = []

    isPointActivated = False
    isSignActivated = False

    for index,ch in enumerate(s):
        if (len(pointBeforDigit) == 0 and isSignActivated == True) and ch == " ":
            break
        if (len(pointBeforDigit) == 0) and ch == " ":
            continue

        

        if len(pointAfterDigit) >= 1 and ch == ".":
            break

        if len(pointAfterDigit) == 0 and ch == ".":
            isPointActivated = True
            continue

        if (ch == "-" or ch == "+") and isSignActivated:
            break

        if len(pointBeforDigit) >= 1 and (ch == "-" or ch == "+"):
            break

        if (ch == "-" or ch == "+") and isSignActivated == False:
            sign = ch
            isSignActivated = True
            continue

        try:
            if int(ch) >= 0:
                if isPointActivated:
                    pointAfterDigit.append(int(ch))
                else:
                    pointBeforDigit.append(int(ch))
                continue
        except:
            break

        # isPointActivated = False
    # print(sign)
    # print(pointBeforDigit)
    # print(pointAfterDigit)
    temp = 0
    while len(pointBeforDigit) > 0:
        temp = temp + pointBeforDigit[0] * (pow(10, len(pointBeforDigit)-1))
        pointBeforDigit.pop(0)

    temp1 = 0

    while len(pointAfterDigit) > 0:
        temp1 = temp1 + pointAfterDigit[0] * (pow(10, len(pointAfterDigit)-1))
        pointAfterDigit.pop(0)

    temp1 = temp1 / pow(10, len(str(temp1)))

    if sign == "-":
        temp = -temp
        temp1 = -temp1

    if temp+temp1 < -2147483648:
        return -2147483648

    if temp + temp1 > 2147483647:
        return 2147483647

    return temp if temp1 == 0 else temp+temp1


# print(myAtoi("00000-42a1234"))
# print(myAtoi("   -42"))
print(myAtoi("  +    413"))
