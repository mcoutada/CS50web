def flip(inp, maxIdx):
    # print(2, id(a))
    strt = 0
    times = len(inp[: maxIdx + 1]) // 2
    while times >= 0:
        inp[strt], inp[maxIdx] = inp[maxIdx], inp[strt]
        strt += 1
        times -= 1


a = [1, 2, 8, 4, 7, 6, 5, 3, 9, 10, 0]
b = []
for i in reversed(range(len(a))):
    maxIdx = a.index(max(a))
    # if you want to alter the list from within the function, you need to pass the full list and not a slice, you can test this behavior by checking the variable id with --> id(a)
    # print(1, id(a))
    flip(a, maxIdx)
    b.insert(0, a.pop(0))

print(b)