def operation(s):
    final = 0

    for each in s:
        if each == "++X" or each == "X++":
            final += 1
        else:
            final -= 1

    return final


print(operation(["--X", "X++", "X++"]))
print(operation(["++X", "++X", "X++"]))
print(operation(["X++", "++X", "--X", "X--"]))
