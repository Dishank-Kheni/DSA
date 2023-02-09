def longestPalindrome(s):
    # find the longest palindrome in a string

    if(len(s) == 0 or len(s) == 1):
        return s
    # repeatCharList = []
    longestPalindromeString = ""
    for i, c in enumerate(s):
        # if c in repeatCharList:
        #     break
        for j in countRepeatChar(i, c, s):
            temp = ""
            temp = s[i:j+1]
            if checkPalindrome(temp):
                if(len(temp) > len(longestPalindromeString)):
                    longestPalindromeString = temp
                    # repeatCharList.append(c)
                    break

    return longestPalindromeString


def countRepeatChar(index, ch, s):
    # count the number of times a character repeats in a string
    count = 0
    repearList = []
    for x in range(index, len(s)):
        if s[x] == ch:
            repearList.append(x)
    return reversed(repearList)


def checkPalindrome(s):
    # check if a string is a palindrome
    isPalindrome = True
    length = len(s)

    i = 0

    while i < length//2:
        if s[i] != s[length-i-1]:
            isPalindrome = False
            break
        i += 1

    # for f, b in (zip(s, s[::-1])):
    #     if f != b:
    #         isPalindrome = False
    #         break

    return isPalindrome


# print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))

print(longestPalindrome("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"))
print(longestPalindrome("aba"))
print(longestPalindrome("252"))
print(longestPalindrome("ccc"))
print(longestPalindrome("AC"))
print(longestPalindrome("a"))
print(longestPalindrome("cbbd"))

# print(temp)
# lastindex = s.find(c, j)
# if lastindex != -1:
#     temp = s[i: lastindex+1]
#     if checkPalindrome(temp):
#         if(len(temp) > len(longestPalindromeString)):
#             longestPalindromeString = temp
# else:
#     if(len(longestPalindromeString) < len(c)):
#         longestPalindromeString = c
