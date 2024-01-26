# Задание 1
# import random
#
# secret_number = random.randint(1, 20)
# user_number = 0
# counter = 3
# print("Number from 1 to 20 is guessed, guess which one of 3 attempts.")
# while secret_number != user_number and counter > 0:
#     user_number = int(input("Enter number [1 - 20] : "))
#     if user_number > secret_number:
#         print("Your number greater than secret")
#         if (user_number - secret_number) > 2:
#             print("You're far enough away")
#         elif (user_number - secret_number) <= 2:
#             print("You're almost there")
#     elif user_number < secret_number:
#         print("Your number less than secret")
#         if (secret_number - user_number) > 2:
#             print("You're far enough away")
#         elif (secret_number - user_number) <= 2:
#             print("You're almost there")
#     counter = counter - 1
#     attempt = f"You have {counter} tries left"
#     print(attempt)
# if user_number == secret_number:
#     print("Congratulations, you guessed it!")
# else:
#     print("It's not your day! You lost!")

# Задание 2
user = input("Enter one letter in the range from 'a' to 'j': ")
a = 10
start = a
c = a
count = 0
symbol = '*'
s = ' '
f = ''
if user == 'a':
    while a > 0:
        print(s * (10 - a) + (symbol * a))
        a = a - 1
elif user == 'b':
    while a > 0:
        print((11 - a) * symbol + (s * a))
        a = a - 1
elif user == 'c':
    while a > 0:
        b = start - a
        if a < start // 2:
            f = f + (s * start) + '\n'
        else:
            f = f + (s * b) + (symbol * c) + (s * b) + '\n'
        c = c - 2
        a = a - 1
    print(f)
elif user == 'd': ##############
    while a > 0:
        b = start - a
        if a > start // 2:
            f = f + (s * start) + '\n'
        else:
            f = f + (s * ) + (symbol * b) + (s * ) + '\n'
        c = c - 2
        a = a - 1
    print(f)

elif user == 'e':
    while a > 0:
        pass