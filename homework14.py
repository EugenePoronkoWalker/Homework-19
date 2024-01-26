# Task 1
# file1 = open('first_page.txt', 'wt')
# file1.write('Hello\n')
# file1.write('My name is Eugene\n')
# file1.write('I am from Kharkiv\n')
# file1.close()
#
# file2 = open('second_page.txt', 'wt')
# file2.write('Hello\n')
# file2.write('My name is Dima\n')
# file2.write('I am from Kiev')
# file2.close()
#
# file1 = open('first_page.txt', 'rt')
# text = file1.readlines()
# file2 = open('second_page.txt', 'rt')
# text2 = file2.readlines()
#
# general_text = text + text2
# for row in general_text:
#     if row not in text or row not in text2:
#         file3 = open('mismatched_strings.txt', 'at')
#         file3.write(str(row))
#         file3.close()
# file1.close()
# file2.close()


#Task 2
# file1 = open('first_page.txt', 'wt')
# file1.write('Hello\n')
# file1.write('My name is Eugene\n')
# file1.write('I am from Kharkiv\n')
# file1.write('I am 30')
# file1.close()
#
# file1 = open('first_page.txt', 'rt')
# text = file1.readlines()
#
# symbol = ''
# new_text = symbol.join(text)
#
# gls = 0
# sgl = 0
# amount_of_rows = 0
# amount_of_symbols = 0
# digits = 0
# all_gls = ['a', 'e', 'i', 'o', 'u', 'y']
# for i in new_text:
#     if i.isalpha():
#         if i in all_gls:
#             gls = gls + 1
#         else:
#             sgl = sgl + 1
#     elif i.isdigit():
#         digits = digits + 1
#     elif i == '\n':
#         amount_of_rows = amount_of_rows + 1
#     amount_of_symbols = amount_of_symbols + 1
#
# results = open('statistics.txt', 'at')
# results.write('Amount of symbols: '+ str(amount_of_symbols))
# results.write('\n')
# results.write('Amount of rows: ' + str(amount_of_rows))
# results.write('\n')
# results.write('Amount of vowel letters: ' + str(gls))
# results.write('\n')
# results.write('Amount of non-vowel letters: ' + str(gls))
# results.write('\n')
# results.write('Amount of digits: ' + str(digits))
# results.close()


#Task 3
# file1 = open('first_page.txt', 'wt')
# file1.write('Hello\n')
# file1.write('My name is Eugene\n')
# file1.write('I am from Kharkiv\n')
# file1.write('I am 30')
# file1.close()
#
# file1 = open('first_page.txt', 'rt')
# text = file1.readlines()
# for row in range (len(text) - 1):
#     file2 = open('list_without_last_row.txt', 'at')
#     file2.write(str(text[row]))
#     file2.close()


#Task 4
# file1 = open('first_page.txt', 'wt')
# file1.write('Hello\n')
# file1.write('My name is Eugene\n')
# file1.write('I am from Kharkiv\n')
# file1.write('I am 30')
# file1.close()
#
# file1 = open('first_page.txt', 'rt')
# text = file1.readlines()
# longest_row = 0
# for row in text:
#     if len(row) > longest_row:
#         longest_row = len(row)
# print(f'The length of the longest line: {longest_row}')
# file1.close()
