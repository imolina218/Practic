# Create a function than giving a string of odd length greater
# than 7, return a string made of the middle three chars of a given String.


# def mid_string():
#     user_input = input("Please enter a word: ")
#
#     if len(user_input) >= 7:
#         length_s = int((len(user_input) / 2) - 1)
#         print("The complete word is {}.".format(user_input))
#         print("The 3 middle letters are {}.".format(user_input[length_s:length_s + 3]))
#         confirmation = input("Would you like to enter another word? yes/no: ")
#         if confirmation in "yes":
#             mid_string()
#         else:
#             print("Bye.")
#     else:
#         print("I'm sorry the word should contain more than 7 letters")
#         confirmation = input("Would you like to try again? yes/no: ")
#         if confirmation in "yes":
#             mid_string()
#         else:
#             print("Bye.")
#
#
# mid_string()
################################
# Given 2 strings, s1 and s2 return a new string made of the first, middle
# and last char each input string.


# def combine_strings():
#     user_input = input("Please enter a word: ")
#     user_input2 = input("Please enter a second word: ")
#     if len(user_input) >= 4 and len(user_input2) >= 4:
#         length_s = int((len(user_input) / 2))
#         length_s2 = int((len(user_input2) / 2))
#         print("The complete words is {}.".format(user_input))
#         print("The mix letters form {}{}{}.".format(user_input[0] + user_input2[0], user_input[length_s] +
#                                                 user_input2[length_s2], user_input[len(user_input)-1] +
#                                                 user_input2[len(user_input2)-1]))
#         confirmation = input("Would you like to enter another word? yes/no: ")
#         if confirmation in "yes":
#             combine_strings()
#         else:
#             print("Bye.")
#     else:
#         print("I'm sorry the word should contain more than 7 letters")
#         confirmation = input("Would you like to try again? yes/no: ")
#         if confirmation in "yes":
#             combine_strings()
#         else:
#             print("Bye.")
#
#
# combine_strings()
#########################################
# Arrange string characters such that lowercase letters should come
# first and the the uppercase letters.

# def lower_then_upper():
#     user_input = input("Please enter a word with uppercase and lowercase: ")
#     lower = ""
#     upper = ""
#     for letter in user_input:
#         if letter.isupper():
#             upper += letter
#         else:
#             lower += letter
#     print(lower+upper)
#
#
# lower_then_upper()
###################################
# Given a string input Count all lowercase, uppercase, digits, and special symbols.
# def is_counter():
#     user_input = input("Please enter a string with various types of characters: ")
#     lower = 0
#     upper = 0
#     digits = 0
#     symbols = 0
#     for char in user_input:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#         elif char.isnumeric():
#             digits += 1
#         else:
#             symbols += 1
#     print("The string have {} lower case, {} upper case, {} digits and {} symbols.".format(lower, upper,
#                                                                                            digits, digits, symbols))
#
#
# is_counter()
##############################
# Create a function that create a third-string made of the first char
# of the last char of b, the second char of the second last char of b, and
# so on. Any leftover chars go at the end of the result.
# def mix_string():
#     str1 = input("Please enter the first word: ")
#     str2 = input("Now enter the second word: ")
#     length1 = len(str1)
#     length2 = len(str2)
#     l1 = 0
#     l2 = length2 - 1
#     length = length1 if length1 > length2 else length2
#     for i in range(length):
#         if i < length1:
#             print(str1[l1], end='')
#             l1 += 1
#         if i < length2:
#             print(str2[l2], end='')
#             l2 -= 1
#
#
# mix_string()
############################################
# Create a program that finds all occurrences of “USA” in given string ignoring the case.
# def usa_detect():
#     str = input('Please enter a string to find how many times "usa" appears: ')
#     keyword = "usa"
#     counter = str.lower().count(keyword)
#     print("The word usa appear {} times in your string.".format(counter))
#
#
# usa_detect()
#######################################
# Create a program that given an input string, count occurrences
# of all characters within a string.
# def letter_type_amount():
#     str1 = input("Enter a string to find how many times each letter appear: ")
#     str_dict = {}
#     for letter in str1:
#         counter = str1.count(letter)
#         str_dict[letter] = counter
#     for k in str_dict:
#         print(k, ":", str_dict[k], sep="", end=" ")
#
#
# letter_type_amount()












