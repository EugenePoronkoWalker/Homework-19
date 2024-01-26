# # Method
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 6, 7, 8, 9}
# # Если просто нужно запринтить
# print(s2.symmetric_difference(s1))
# # Если нужно создать отдельное множество
# s3 = {}
# s3 = s2.symmetric_difference(s1)
# print(s3)

# #Cycle
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 2, 6, 7, 8, 9}
# s3 = set()
# s3 = s1.union(s2)
# s4 = set()
# for i in s3:
#     if i in s1 and i in s2:
#         print(f'{i} is exist in two sets')
#     else:
#         s4.add(i)
# print(f'This is a new set: {s4}')
#
#
#
# l = [1, 5, 3, 7, 8, 3, 9, 10, -1, 5, 0, 45]
# amount = len(l)
# for elem in range(amount - 1):
#     for elem2 in range(amount - elem -1):
#         if l[elem2] > l[elem2 + 1]:
#             l[elem2], l[elem2 + 1] = l[elem2 + 1], l[elem2]
#
# print(l)