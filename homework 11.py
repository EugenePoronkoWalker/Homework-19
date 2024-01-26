# Task1
# def show_text():
#     text = '''"Don't compare yourself with anyone in this world... \n if you do so, you are insulting yourself." \n Bill Gates'''
#     return text
#
#
# print(show_text())
# Task2
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     b, a = a, b
# print(a, b)
#
#
# def show_even_numbers(start, finish):
#     result = []
#     for i in range(start + 1, finish):
#         if i % 2 == 0:
#             result.append(i)
#     return f'List of even numbers : {result}'
#
#
# print(show_even_numbers(a, b))
# Task3
# length = int(input("Enter a length of square: "))
# symbol = str(input("Enter a symbol: "))
# action = str(input("Enter an action 'True' or 'False' :"))
#
#
# def show_square(length, symbol, action):
#     if action == 'True':
#         for i in range(length):
#             print(symbol * length)
#     else:
#         for i in range(length):
#             if i == 0 or i == (length - 1):
#                 print(symbol * length)
#             else:
#                 print(symbol + ' ' * (length - 2) + symbol)
#
#
# show_square(length, symbol, action)
# Task4
# def show_minimum_number():
#     amount_of_numbers = 5
#     list_of_number = []
#     for i in range(amount_of_numbers):
#         number = int(input("Enter number: "))
#         list_of_number.append(number)
#     return min(list_of_number)
#
#
# print(show_minimum_number())
# Task5
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     b, a = a, b
# print(a, b)
#
#
# def multiply_numbers(start, finish):
#     result = 1
#     for i in range(start, finish + 1):
#         result = result * i
#     return f'Multiply numbers in range from {a} to {b} is equal {result}'
#
#
# print(multiply_numbers(a, b))
# Task6
# number = int(input("Enter a number: "))
#
#
# def calculate_amount_numbers(number):
#     new_list = []
#     while number > 0:
#         new_list.append(number % 10)
#         number = number // 10
#     return len(new_list)
#
#
# print(calculate_amount_numbers(number))
# Task7
# number = int(input("Enter number: "))
#
#
# def change_to_list(number):
#     full_list = []
#     while number > 0:
#         full_list.append(number % 10)
#         number = number // 10
#     full_list.reverse()
#     return full_list
#
#
# def show_palindrom(number):
#     if len(change_to_list(number)) % 2 != 0:
#         print(f'This {number} is not a palindrom')
#     else:
#         half_full_list = int(len(change_to_list(number)) / 2)
#         first_list = change_to_list(number)[:half_full_list]
#         second_list = change_to_list(number)[half_full_list:]
#         second_list.reverse()
#         if first_list == second_list:
#             print(f'This {number} is a palindrom')
#         else:
#             print(f'This {number} is not a palindrom')
#
#
# show_palindrom(number)
