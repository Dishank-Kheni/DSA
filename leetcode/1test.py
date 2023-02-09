# c = {2: ["abc", 0], 3: ["dbc", 1], 2: ["dcv", 2]}
# c = ({2, ["abc", 0]})
# # print(c.get(3)[0])

# # print(c.fromkeys(2))
# print([(k, v) for k, v in c.items()])
# print(c.get(2))
# print(c.__getitem__(6))


key = [2, 3, 2]
value = [["abc", 0], ["dbc", 1], ["dcv", 2]]

d = [(k, v) for k, v in zip(key, value) if k == 2]
print(d[0][1])
