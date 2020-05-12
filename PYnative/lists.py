# Take a list and reverse it.
# a_lsit = [100, 200, 300, 400, 500]
# print(a_lsit)
# # a_lsit.reverse()
# print(a_lsit[::-1])
# print(a_lsit)
##################################################
# Concatenate the following two lists index-wise.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i, j in zip(list1, list2)]
# list3 = list
# for i, j in zip(list1, list2):
#     list3 = i + j
# print(list3)
##################################################
# Given a python list. Turn every time of a list into its square.
# aList = [1, 2, 3, 4, 5, 6, 7]
# list1 = [i**2 for i in aList]
# print(list1)
##################################################
# Concatenate two lists in the following order : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = [x + y for x in list1 for y in list2]
# print(list3)
##################################################
# Given a two Python list. Iterate both lists simultaneously such that list1
# should display item in original order and list2 in reverse order.
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)
##################################################
# Remove the empty strings from the list of strings.
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list_result = list(filter(None, list1))
# print(list_result)
##################################################
# Add item 7000 after 6000 in the following Python List.
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
##################################################
# Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look
# like the following list: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'].
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# print(list1)
# list_to_add = ["h", "i", "j"]
# print(list_to_add)
# list1[2][1][2].extend(list_to_add)
# print(list1)
##################################################
# Given a Python list, find value 20 in the list, and if it is
# present, replace it with 200. Only update the first occurrence of a value.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = list1.index(20)
# list1[index] = 200
# print(list1)
##################################################
# Given a Python list, remove all occurrence of 20 from the list.
list1 = [5, 20, 15, 20, 25, 50, 20]


def remove_element(l_ist, x):
    return [l_ist.remove(i) for i in l_ist if i == 20]
    # for i in l_ist:
    #     if i == x:
    #         l_ist.remove(i)
    # print(l_ist)


remove_element(list1, 20)
print(list1)













