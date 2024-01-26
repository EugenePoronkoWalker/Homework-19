# Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник,
# 2 — вторник и т.д.
# Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.
# Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»
# Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.
# Задание 5
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран сумму трёх чисел или произведение трёх чисел.
# Задание 6
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

# Задание 1:
day = input('Enter the day of the week: ')
if day == 'Monday':
    print(1)
elif day == 'Tuesday':
    print(2)
elif day == 'Wednesday':
    print(3)
elif day == 'Thursday':
    print(4)
elif day == 'Friday':
    print(5)
elif day == 'Saturday':
    print(6)
elif day == 'Sunday':
    print(7)
else:
    print('Error')

# Задание 2
month = int(input('Enter the number of month: '))
if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
elif month == 4:
    print('April')
elif month == 5:
    print('May')
elif month == 6:
    print('June')
elif month == 7:
    print('Jule')
elif month == 8:
    print('August')
elif month == 9:
    print('September')
elif month == 10:
    print('October')
elif month == 11:
    print('November')
elif month == 12:
    print('December')
else:
    print('Entered number of month is not exist')

# Задание 3:
number = int(input('Enter a number: '))
if number >= 1:
    print('Number is positive')
elif number == 0:
    print('Number is equal to zero')
elif number < 0:
    print('Number is negative')
else:
    print('Error')

# Задание 4:
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
if num1 == num2:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
elif num1 != num2:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
else:
    print('Error')

# Задание 5:
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
action = input("Enter an action: '+' or '*': ")
result = ''
if action == '+':
    result = f"{num1} {action} {num2} {action} {num3} = {num1 + num2 + num3}"
elif action == '*':
    result = f"{num1} {action} {num2} {action} {num3} = {num1 * num2 * num3}"
else:
    print('Error')
print(result)

# Задание 6:
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
action = input("Enter an action: 'max', 'min' or 'arithmetic': ")
result = ''
if action == 'max':
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3:
        print(num2)
    else:
        print(num3)
elif action == 'min':
    if num1 < num2 and num1 < num3:
        print(num1)
    elif num2 < num3:
        print(num2)
    else:
        print(num3)
elif action == 'arithmetic':
    print((num1 + num2 + num3) / 3)
else:
    print('Error')