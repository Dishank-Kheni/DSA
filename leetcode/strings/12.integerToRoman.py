def romanToInt(num):
    # romanKey = {1: "I", 5: "V", 10: "X",
    #             50: "L", 100: "C", 500: "D", 1000: "M"}

    square = len(str(num))
    romanStr = ""

    for digit in str(num):
        digit = int(digit)
        if digit == 0:
            square -= 1
            continue

        if square == 4:
            romanStr = romanStr + "M" * digit

        if square == 3:
            if digit == 4:
                romanStr = romanStr + "CD"
                square -= 1
                continue
            if digit == 9:
                romanStr = romanStr + "CM"
                square -= 1
                continue

            if digit < 5:
                romanStr = romanStr + "C" * digit

            if digit > 5:
                romanStr = romanStr + ("D" + ("C"*(digit-5)))

            if digit == 5:
                romanStr = romanStr + "D"

        if square == 2:
            if digit == 4:
                romanStr = romanStr + "XL"
                square -= 1
                continue
            if digit == 9:
                romanStr = romanStr + "XC"
                square -= 1
                continue

            if digit < 5:
                romanStr = romanStr + "X" * digit

            if digit > 5:
                romanStr = romanStr + ("L" + ("X"*(digit-5)))

            if digit == 5:
                romanStr = romanStr + "L"

        if square == 1:
            if digit == 4:
                romanStr = romanStr + "IV"
                square -= 1
                continue
            if digit == 9:
                romanStr = romanStr + "IX"
                square -= 1
                continue

            if digit < 5:
                romanStr = romanStr + "I" * digit

            if digit > 5:
                romanStr = romanStr + ("V" + ("I"*(digit-5)))

            if digit == 5:
                romanStr = romanStr + "V"
        square -= 1

    return romanStr


# print(romanToInt(3))
print(romanToInt(58))
print(romanToInt(1994))
