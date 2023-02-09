def convert(s, x):

    # print string in zigzag pattern

    # if x == 1:
    #     print(s)
    #     return

    finalConversion = []

    for i in range(x):
        # temp = 1
        upToogle = False
        # FirstTime = True
        downindex = (x-i-1)+(x-2-i)+1
        upindex = i*2
        # spaceTime = x - 2 - i

        j = i

        while(j < len(s)):
            if i == 0 or i == x-1:
                if upToogle == False:
                    finalConversion.append(s[j])
                    # print(s[j], end=' ' * int(x-2))
            # else:
            #     if i == x-2:
            #         if temp != 2:
            #             temp += 1
            #             print(s[j], end='')
            #         else:
            #             temp = 1
            #             print(s[j], end=' ' * int(x-3))
            #     elif i == 1:
            #         if FirstTime:
            #             print(s[j], end=' ' * int(x-3))
            #             FirstTime = False
            #         else:
            #             if temp != 2:
            #                 temp += 1
            #                 print(s[j], end='')
            #             else:
            #                 temp = 1
            #                 print(s[j], end=' ' * int(x-3))
            else:
                finalConversion.append(s[j])
                # print(s[j], end=" " * int(spaceTime))
            if upToogle:
                j += upindex
                upToogle = False
            else:
                j += downindex
                upToogle = True
        # print("\n")

    return ''.join(finalConversion)


print(convert("paypalishiring", 1))
