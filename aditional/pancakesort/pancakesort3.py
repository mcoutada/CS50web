from random import shuffle


def flip(inp):
    tot = len(inp)
    for i in range(tot // 2):
        inp[i], inp[tot - 1 - i] = inp[len(inp) - 1 - i], inp[i]
    return inp


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
shuffle(a)
print(f"Unsorted: {a}")

while a:
    maxIdx = a.index(max(a))
    a[: maxIdx + 1] = flip(a[: maxIdx + 1])
    b.insert(0, a.pop(0))

print(f"  Sorted: {b}")
