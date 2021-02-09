from random import shuffle

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(a)
print(f"Unsorted: {a}")


for i in reversed(range(len(a))):
    maxIdx = a[: i + 1].index(max(a[: i + 1]))
    a[: maxIdx + 1] = a[: maxIdx + 1][::-1]
    a = a[1 : i + 1] + a[:1] + a[i + 1 :]

print("Sorted: ", a)
