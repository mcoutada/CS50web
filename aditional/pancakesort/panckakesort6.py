a = [3, 1, 2, 4, 5, 7, 9, 8, 0]


def flip(inp, maxpos):
    return inp[: maxpos + 1][::-1] + inp[maxpos + 1 :]


def pancakesort(lst):
    
    for i in range(lst):
        sorted = lst[-i:]
        tosort = lst[:-i]
        maxidx = tosort.index(max(lst))
        tosort = flip(lst, maxidx)
            return tosort[1:] + lst[:1]


b = pancakesort(a)
print(b)
