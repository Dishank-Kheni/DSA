def lengthOfLastWord(s):
    lastWord = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] == " " and lastWord == "":
            continue
        else:
            if s[i] == " ":
                break
            else:
                lastWord += s[i]

    return len(lastWord)


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("Hello World "))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
