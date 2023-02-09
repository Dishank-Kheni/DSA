
def fullJustify(words, maxWidth):
    finalList = []
    i = 0
    while i < len(words):
        tempList = []
        remainSpace = maxWidth
        wordCount = 0
        k = 0
        for j in range(i, len(words)):
            length = len(words[j])

            if k == 0:
                if length <= remainSpace:
                    tempList.append(words[j])
                    remainSpace = remainSpace - length
                    wordCount += 1
                    i += 1
                    k += 1
                else:
                    break
            else:
                if length + 1 <= remainSpace:
                    tempList.append(" "+words[j])
                    wordCount += 1
                    remainSpace = remainSpace - (length+1)
                    i += 1
                    k += 1
                else:
                    break

        if remainSpace == 0:
            finalList.append(tempList)
            continue

        if i == len(words):
            tempList.append(" "*remainSpace)
            finalList.append(tempList)
            break

        if wordCount <= 2:
            tempList.insert(1, " "*remainSpace)
            finalList.append(tempList)
            continue

         # if remainSpace <= wordCount:
        #     for j in range(1, remainSpace+1):
        #         tempList[j] = "_" + tempList[j]
        #     remainSpace -= 1
        # else:
        while remainSpace != 0:
            for j in range(1, wordCount):
                tempList[j] = " "+tempList[j]
                remainSpace -= 1

                if remainSpace == 0:
                    break

            # while remainSpace != 0:
            #     for j in range(1, wordCount):
            #         tempList[j] = "_"+tempList[j]
            #         remainSpace -= 1

        finalList.append(tempList)
    returnList = []
    for  each in finalList:
        # finalList.remove(each)
        str1 = ""
        for k in range(len(each)):
            # print(each[k])
            str1 = str1 + str(each[k])
        print(str1)
        # str(str1).replace("_", " ")
        returnList.append(str1)
    
    
    # finalList.insert(index, each)
# print(returnList)
    return returnList