def combination(digits):
    phoneKey = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "xyzw"}

    trackingList = []

    def rec_fun(s, track):
        if track == len(digits):
            trackingList.append(s)
            return

        for ch in phoneKey.__getitem__(digits[track]):
            rec_fun(s + ch, track+1)

    rec_fun("", 0)
    return trackingList


print(combination(""))
# print(combination("23456789"))
