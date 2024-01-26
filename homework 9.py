l = [1, 5, 3, 7, 8, 3, 9, 10, -1, 5, 0, 45]
amount = len(l)
for elem in range(amount - 1):
    for elem2 in range(amount - elem -1):
        if l[elem2] > l[elem2 + 1]:
            l[elem2], l[elem2 + 1] = l[elem2 + 1], l[elem2]

print(l)
