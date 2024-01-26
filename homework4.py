# Задание 1:
num1 = int(input('Enter first number: '))    # Неверно сделано!
num2 = int(input('Enter second number: '))
counter = 1
if num1 > num2:
    c = num1
    num1 = num2
    num2 = c
while num1 <= num2:
    while counter <= num1:
        if num1 % counter != 0:
            print(counter, end=' ')
        counter = counter + 1
    num1 = num1 + 1

# Задание2:
# num = 1
# max_num = 10
# result = 0
# counter = 1
# while num <= max_num:
#     while counter <= max_num:
#         result = f"{num} * {counter} = {num * counter}"
#         counter = counter + 1
#         print(result)
#     num = num + 1
#     counter = 1
#     print('-' * 10)


# Задание 3
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# max_num = 10
# counter = 1
# result = 0
# if num1 > num2:
#     c = num1
#     num1 = num2
#     num2 = c
# while num1 <= num2:
#     while counter <= max_num:
#         result = f"{num1} * {counter} = {num1 * counter}"
#         counter = counter + 1
#         print(result)
#     num1 = num1 + 1
#     counter = 1
#     print('-' * 10)
