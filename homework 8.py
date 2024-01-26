# # Task 1
line = str(input())
new_line = line[::-1]
if line.lower().replace(' ','') == new_line.lower().replace(' ',''):
    print("Entered string is a palindrome")
else:
    print("Entered string isn't palindrome")

# Task 3
text = str(input("Enter a text: "))
symbol = '.!?'
counter = 0
for i in range(len(text)):
    if text[i] in symbol:
        counter = counter + 1
print(counter)

# # Task 2
# text = str(input("Enter a text: "))
# words = str(input("Enter words: "))
# for element in words:
#     text = text.replace(element, element.upper())
# print(text)