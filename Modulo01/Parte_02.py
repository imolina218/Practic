# 01. Create a function call max_in_list() that takes a list of numbers and returns the max.
# def max_in_list(x):
#     max_number = 0
#     for i in x:
#         if i > max_number:
#             max_number = i
#         else:
#             continue
#     print(max_number)
#
#
# max_in_list([3, 5, 7, 2, 4, 9, 14])

# 02. Create a function call longer() that takes a list of words and print the longer one.
# def longest(x):
#     longer_word = ""
#     for i in x:
#         if len(i) > len(longer_word):
#             longer_word = i
#     print(longer_word)
#
#
# longest(["hoal", "asidusa", "asdouiahgd", "oj"])

# 03. Create a function call word_filter() that takes a list of words and takes an integer
# and prints the words that are longer than the integer argument.


# def word_filter(list_words, integer):
#     integer = int(integer)
#     words_longer = []
#     for i in list_words:
#         if len(i) > integer:
#             words_longer.append(i)
#     print(words_longer)
#
#
# word_filter(["suzuki", "yamaha", "indian", "bmw", "taca"], 4)

# 04. Create a program that ask the user to input an string, then count the uppercase letters and print them.
# user_input = input("Please enter a text string, with uppercase letters.")
# upper_count = 0
# for i in user_input:
#     if i != i.lower():
#         upper_count += 1
# print(upper_count)

# 05. Build a program that converts a binary number to int.
# def binary_to_decimal(binary_num):
#     binary_num = str(binary_num)
#     decimal = 0
#     exp = len(binary_num) - 1
#     for i in binary_num:
#         decimal += (int(i) * 2 ** (exp))
#         exp = exp - 1
#     print(decimal)
#
#
# binary_to_decimal("011101011")

# 06. Write a program where the user input current year, 3 names and the year they was born
# and calculate how many years are going to have in the current year.
# def main():
#     current_year = input("Please enter the current year: ")
#     current_year = int(current_year)
#     for i in range(3):
#         user_name = input("Please enter a name: ")
#         user_year_born = input("Please enter the year that born: ")
#         user_year_born = int(user_year_born)
#         years_old = current_year - user_year_born
#         print("This {0} {1} will be {2} years old.".format(current_year, user_name, years_old))
#
#
# main()

# 07. Define a tuple with 10 different ages and print how many people are older than 20 years old.
# def sup_to_20(tup):
#     older_than_20 = 0
#     for i in tup:
#         if i > 20:
#             # older_than_20.append(i)
#             older_than_20 += 1
#     print(older_than_20)
#
#
# sup_to_20((5, 13, 56, 89, 23, 16, 19, 36, 67, 11))
# TRY TO DO THE SAME BUT WITH NAMES #TODO

# 08. Create a function that take a list of names and print the names that start with a.
# then let the user choose the letter.
# def first_letter(x):
#     letter_to_search = input("Enter the first letter of the name you are looking for: ").lower()
#     list_names = []
#     for i in x:
#         if i[0].lower() == letter_to_search:
#             list_names.append(i)
#     print(list_names)
#
#
# first_letter(["Astra", "Ismael", "Ashley", "Marley", "abu", "Lean", "Tim", "nic", "Leo"])

# 09. Create a function vocal_counter() that count how many of each vocal have in the string.
# then make the user input the word to search.
# def vocal_counter(string):
#     string = string.lower()
#     vowels = "aeiou"
#     for i in vowels:
#         counter = 0
#         for x in string:
#             if x == i:
#                 counter += 1
#         print("There is {} {}".format(counter, i))
#
#
# vocal_counter("Ismaele")

# 10. Create a function is_leap() that define if a year is leap. A leap day is divisible by 4
# but not for 100 and also divisible by 400.
# def main(year):
#     year = int(year)
#     if year % 4 == 0 and year % 400 == 0:
#         print("The year {} introduce is a leap year".format(year))
#     else:
#         print("The year {} is not a leap year".format(year))
#
#
# main(2020)





















