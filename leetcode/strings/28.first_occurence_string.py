def strStr(haystack, needle):
    needleTracker = 0
    i = 0
    listTracker = []
    while i < len(haystack):
        if haystack[i] == needle[0] and needleTracker >= 1:
            listTracker.append(i)
        if haystack[i] == needle[needleTracker]:
            needleTracker += 1
        else:
            needleTracker = 0
            if listTracker != []:
                i = listTracker.pop(0)
                continue
                # list = []

        if needleTracker == len(needle):
            print(i - needleTracker + 1)
            needleTracker = 0

        i += 1

    # for index in range(len(haystack)):
    #     if haystack[index] == needle[needleTracker]:
    #         needleTracker += 1
    #     else:
    #         needleTracker = 0

    #     if needleTracker == len(needle):
    #         return index - needleTracker + 1
    return -1


# print(strStr("hello", "ll"))
# print(strStr("aaaaa", "bba"))
# print(strStr("a", "a"))
# print(strStr("mississippi", "issip"))
print(strStr("a", "a"))
# print(strStr("foobarfoobar", "barfoo"))
