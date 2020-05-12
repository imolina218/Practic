# 01. Create a function call max that takes 2 arguments and give back de max number.
# Python have already a built on function call max, but for a better practice
# don't use that function.


# def max(number1, number2):
#     number1 = int(number1)
#     number2 = int(number2)
#     if number1 > number2:
#         print("{} is greater than {}".format(number1, number2))
#     elif number2 > number1:
#         print("{0} is greater than {1}".format(number2, number1))
#     else:
#         print("The numbers are equal")
#
#
# max(4, 8)

# 02. Create a function call max_of_three(), that takes 3 numbers as arguments and return the grater


# def max_of_three(number1, number2, number3):
#     if number1 > number2 and number1 > number3:
#         print("{} is greater than {} and {}".format(number1, number2, number3))
#     elif number2 > number1 and number2 > number3:
#         print("{} is greater than {} and {}".format(number2, number1, number3))
#     elif number3 > number1 and number3 > number2:
#         print("{} is greater than {} and {}".format(number3, number1, number2))
#     else:
#         print("The numbers are equal.")
#
#
# max_of_three(3, 6, 7)

# 03. Create a function that calculate the length of a list without using the function len()

# def length(list):
#     counter = 0
#     for i in list:
#         counter += 1
#     print(counter)
#
#
# length([1, 23, 4, 54])

# 04. Create a function that takes a character and return True if it's a vocal

# def if_vocal(x):
#     vowels = "aeiou"
#     if x in vowels:
#         print(True)
#     else:
#         print(False)
#
#
# if_vocal("s")

# 05. Create a function sum() and a function multi() that returns the values
# of a list added and multiply.

# def sum(x):
#     added = 0
#     for i in x:
#         added += i
#     print(added)
#
#
# def multi(x):
#     multiply = 1
#     for i in x:
#         multiply *= i
#     print(multiply)
#
#
# sum([1, 2, 3, 4])
# multi([1, 2, 3, 4])

# 06. Create a function inverse() that calculates the inverse of a string.

# def inverse(x):
#     inv = x[::-1]
#     print(inv)
#
#
# inverse("hola")

# 07. Create a function is_palindrome() that returns True is the word backwards is the same.

# def is_palindrome(x):
#     inv = x[::-1]
#     if inv == x:
#         print(True)
#
#
# is_palindrome("radar")

# 08. Create a function superposition() that takes two lists and return True if they have
# any character in common.
# def superposition(x, y):
#     for i in x:
#         for e in y:
#             if i == e:
#                 print(True)
#
#
# superposition([1, 23, 4, 5], [6, 8, 0, 23])

# 09. Create a function call characters_n_generator() that takes a int and then multiply it for
# for the second argument.

# def characters_n_generator(x, y):
#     x = int(x)
#     y = str(y)
#     print(x * y)
#
#
# characters_n_generator(5, "s")

# 10. Create a function call procedure() that takes a list of integer numbers and print an histogram.

# def procedure(x):
#     for i in x:
#         print("*"*i)
#
#
# procedure([4, 5, 6])











