def lengthOfLongestSubstring(s):
    # return the length of the longest substring without repeating characters
    temp = ""
    final = ""
    for i, ch in enumerate(s):
        if ch not in temp:
            temp += ch
            # print(i, len(s))
            if i == (len(s)-1):
                if len(final) < len(temp):
                    final = temp
                # list.append(temp)

        else:
            if len(final) < len(temp):
                final = temp
            # list.append(temp)
            temp += ch
            for j, c in enumerate(temp):
                if c == ch:
                    temp = temp[j+1:]
                    break

    return len(final)
    # return 1 if len(list) == 0 else len(list)


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("au")
lengthOfLongestSubstring("dvdf")
lengthOfLongestSubstring("c")
lengthOfLongestSubstring("")
# lengthOfLongestSubstring(" ")
