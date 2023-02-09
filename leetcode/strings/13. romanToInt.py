def romanToInt(s):
    romanKey = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}

    index = -1

    temp = 0

    while(index >= -len(s)):

        try:
            if s[index-1]+s[index] == "IV":
                temp = temp + 4
                index -= 2
                continue

            if s[index-1]+s[index] == "VX":
                temp = temp + 9
                index -= 2
                continue

            if s[index-1]+s[index] == "XL":
                temp = temp + 49
                index -= 2
                continue

            if s[index-1]+s[index] == "XC":
                temp = temp + 90
                index -= 2
                continue

            if s[index-1]+s[index] == "CD":
                temp = temp + 400
                index -= 2
                continue

            if s[index-1]+s[index] == "CM":
                temp = temp + 900
                index -= 2
                continue

        except:
            pass

        temp = temp + romanKey.__getitem__(s[index])
        index -= 1

    return temp


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
