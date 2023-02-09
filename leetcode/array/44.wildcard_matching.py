
def isMatch(s, p):
    

# def isMatch(s, p):
#     # match string to particular pattern
#     if p == "*":
#         temp = s[0]
#         for i in s:
#             if i != temp:
#                 return False
#         return True
#     elif p[0] == "?":
#         temp = p[1]
#         for i in range(len(s)-1):
#             if s[i+1] != temp:
#                 return False
#         return True
#     else:
#         try:
#             for i in range(len(s)):
#                 if s[i] != p[i]:
#                     return False
#         except:
#             return False
#         return True


# print(isMatch("aa", "aa"))
# print(isMatch("aa", "*"))
# print(isMatch("cb", "?a"))
