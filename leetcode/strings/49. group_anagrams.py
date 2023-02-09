def groupAnagrams(strs):

    def ordSum(str):
        temp = 0
        for ch in str:
            temp = temp + ord(ch)

        return temp

    def charCmp(str1, str2):
        for ch in str1:
            if ch not in str2:
                return False

        return True

    traceDict = {}
    key = []
    value = []

    list = []

    for word in strs:
        sum = ordSum(word)
        metaDict = [(k, v) for k, v in zip(key, value) if k == sum]
        # metaDict = traceDict.get(sum)
        if(metaDict == []):
            list.append([word])
            key.append(sum)
            value.append([word, len(list)-1])
            # traceDict.__setitem__(sum, )
        else:
            for i in range(len(metaDict)):
                if charCmp(metaDict[i][1][0], word):
                    list[metaDict[i][1][1]].append(word)
                else:
                    list.append([word])
                    key.append(sum)
                    value.append([word, len(list)-1])

    return list


# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(groupAnagrams(["ddddddddddg", "dgggggggggg"]))
# print(groupAnagrams(["cab", "tin", "pew", "duh",
#       "may", "ill", "buy", "bar", "max", "doc"]))

print(groupAnagrams(["vow", "pam", "vic", "bee", "ken", "jay", "oft", "sue", "joy", "yuk", "sac", "mac", "inc", "big", "icy", "bus", "lob", "flo",
      "day", "aol", "eel", "rex", "jug", "man", "cod", "mix", "guy", "ken", "ion", "meg", "tot", "noe", "ref", "ito", "inn", "van", "cry", "tad"]))

# print(groupAnagrams(["ken", "dev", "ken"]))
