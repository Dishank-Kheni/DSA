def findSubstring(s, words):

    def rec_fun(s, rec_per):
        if len(s) == 2:
            pair1 = rec_per + s[0] + s[1]
            # s.reverse()
            pair2 = rec_per + s[1] + s[0]

            trackingList.append(pair1)
            trackingList.append(pair2)
            return

        for i, ch in enumerate(s):
            s_copy = s[:]
            popWord = s_copy.pop(i)
            rec_per_copy = rec_per
            rec_per_copy = rec_per_copy + popWord

            rec_fun(s_copy, rec_per_copy)

    trackingList = []
    if len(words) <= 1:
        trackingList.append(words)
        # trackingList = words
    else:
        rec_fun(words, "")
    indexList = []

    for word in trackingList:
        needleTracker = 0
        i = 0
        listTracker = []
        # index = s.find(word)
        # if index != -1 and index not in indexList:
        #     indexList.append(index)

        while i < len(s):
            if s[i] == word[0] and needleTracker >= 1:
                listTracker.append(i)
            if s[i] == word[needleTracker]:
                needleTracker += 1
            else:
                needleTracker = 0
                if listTracker != []:
                    i = listTracker.pop(0)
                    continue
                    # list = []

            if needleTracker == len(word):
                # break
                # print((i - needleTracker + 1))
                if ((i - needleTracker + 1) != -1 and (i - needleTracker + 1) not in indexList):
                    indexList.append(i - needleTracker + 1)
                needleTracker = 0
                if listTracker != []:
                    i = listTracker.pop(0)
                    continue
                # continue

            i += 1

    return indexList


# print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
# print(findSubstring("wordgoodgoodgoodbestword",
#       ["word", "good", "best", "word"]))
# print(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

# print(findSubstring("a", ["a"]))
# print(findSubstring("aaa", ["a", "a"]))
print(findSubstring("bcabbcaabbccacacbabccacaababcbb",
      ["c", "b", "a", "c", "a", "a", "a", "b", "c"]))

# print(findSubstring("mississippi", ["is"]))
print(findSubstring("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel", [
      "dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]))
