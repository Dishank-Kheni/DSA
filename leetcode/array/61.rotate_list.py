def rotateRight(head, k):
    length = len(head)
    times = k
    if k < length:
        times = k
    else:
        times = length % k
        times += 1

    for i in range(times):
        first = head.pop()
        head.insert(0, first)
    return head


print(rotateRight([1, 2, 3, 4, 5], 2))
print(rotateRight([0, 1, 2], 4))
