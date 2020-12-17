from random import shuffle


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
shuffle(a)
print(f"Unsorted: {a}")


while a:
    max_index = a.index(max(a))
    a[: max_index + 1] = a[: max_index + 1][::-1]
    b = a[:1] + b
    a = a[1:]

print("Sorted: ", b)
