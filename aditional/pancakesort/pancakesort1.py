from random import shuffle


def pancakesort(lst):
    a = []
    b = []
    a[:] = lst
    for _ in range(len(a)):
        maxIdx = a.index(max(a))
        for j in range((maxIdx + 1) // 2):
            print("-" * 50 * (j == 0))
            print(f"{a} {b} --> flip {a[j]} with {a[maxIdx-j]}")
            a[j], a[maxIdx - j] = a[maxIdx - j], a[j]
        print("-" * 50)
        b.insert(0, a.pop(0))
        print(f"{a} {b} --> {b[0]} inserted")
    return b


c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(c)
print(f"\nUnsorted: {c}\n")

d = pancakesort(c)

print(f"\nSorted: {d}\n")
assert d == sorted(c)
