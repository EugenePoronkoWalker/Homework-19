# Task1
#
# def multiply_numbers(lst):
#     counter = 1
#     for i in lst:
#         counter = counter * i
#     return f'The result of multiplying numbers is {counter}'
#
#
# lst_numbers = [2, 4, 6, 8, 123]
# print(multiply_numbers(lst_numbers))


# Task2

# def find_minimum_number(lst):
#     minimal_value = min(lst)
#     return f'The minimal number is {minimal_value}'
#
#
# lst_numbers = [2, 4, 7, 10, -3]
# print(find_minimum_number(lst_numbers))

# Task3
#
# def find_amount_simple_number(lst):
#     counter = 0
#     new_list = []
#     for i in lst:
#         for j in range(1, i + 1):
#             if i % j == 0 or i / j == i:
#                 counter = counter + 1
#         if counter == 2:
#             new_list.append(i)
#         counter = 0
#     return f'Amount of simple numbers in the list : {len(new_list)}'
#
#
# lst_numbers = [4, 3, 5, 4, 8, 18, 23, 25, 24]
# print(find_amount_simple_number(lst_numbers))
# Task4
# def show_amount_deleted_numbers(*args, list_numbers):
#     counter = 0
#     for i in args:
#         if i in list_numbers:
#             list_numbers.remove(i)
#             counter = counter + 1
#     return f'Amount of deleted numbers: {counter}'
#
#
# print(show_amount_deleted_numbers(2, 3, 4, list_numbers=[2, 5, -10, 3, 15]))

# Task5
# def show_common_elements_of_lists(list1, list2):
#     new_list = []
#     for i in list1:
#         if i in list2:
#             new_list.append(i)
#     return f'The list with common numbers: {new_list}'
#
#
# lst_numbers1 = [1, 2, 6, 7, 25]
# lst_numbers2 = [32, 2, 7, -1]
# print(show_common_elements_of_lists(lst_numbers1, lst_numbers2))

# Task6
#
# def calculate_degree_of_each_element(degree, lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i ** degree)
#     return f'The new list with elements in entered degree: {new_list}'
#
#
# degree = 2
# lst_numbers = [2, 3, 4, 5]
# print(calculate_degree_of_each_element(degree, lst_numbers))
