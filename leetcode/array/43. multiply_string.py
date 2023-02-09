

def multiply(num1, num2):
    # return multiplication of two int in string format

    def asciiToInt(num):
        if num == "48":
            return 0
        if num == "49":
            return 1
        if num == "50":
            return 2
        if num == "51":
            return 3
        if num == "52":
            return 4
        if num == "53":
            return 5
        if num == "54":
            return 6
        if num == "55":
            return 7
        if num == "56":
            return 8
        if num == "57":
            return 9

    list1 = []
    list2 = []
    for num in num1:
        list1.append(asciiToInt(num))

    print(list1)
    a = "a"
    print(a)
