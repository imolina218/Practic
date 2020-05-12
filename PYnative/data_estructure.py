# Create a function that given a two list. Create a third list by
# picking an odd-index element from the first list and even index
# elements from second.


# def even_odd_list():
#     listOne = [3, 6, 9, 12, 15, 18, 21]
#     listTwo = [4, 8, 12, 16, 20, 24, 28]
#     listthree = list()
#     odds = listOne[1::2]
#     even = listTwo[::2]
#     listthree.extend(odds + even)
#     print(listthree)
#
#
# even_odd_list()
############################
# Create a function that Given an input list removes
# the element at index 4 and add it to the 2nd position and also, at the end of the list.


# def add_element():
#     list = [34, 54, 67, 89, 11, 43, 94]
#     element = list.pop(4)
#     list.insert(2, element)
#     list.append(element)
#     print(list)
#
#
# add_element()
###########################################################
# Create a function that given a list slice it into a 3 equal chunks and rever each list
# def div_by_three():
#     sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#     length = int(len(sampleList)/3)
#     for i in range(1, 4, 1):
#         index = slice(0, length, 1)
#         slice_list = sampleList[index]
#         print("Slice1", i, slice_list)
#         print("Reverse slice", slice_list.reverse())
#     start = length
#
#
# div_by_three()
##################################
# Create a function that Given a list iterate it and count the occurrence
# of each element and create a dictionary to show the count of each element.
# def create_dict_counter():
#     list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#     list1_dict = dict()
#     for num in list1:
#         if num in list1_dict:
#             list1_dict[num] += 1
#         else:
#             list1_dict[num] = 1
#     print(list1_dict)
#
#
# create_dict_counter()
#####################################
# Create a function that given a two list of equal size create a set such that
# it shows the element from both lists in the pair.
# def pair_set_gen():
#     list1 = [2, 3, 4, 5, 6, 7, 8]
#     list2 = [4, 9, 16, 25, 36, 49, 64]
#
#     result = zip(list1, list2)
#     result = set(result)
#     print(result)
#
#
# pair_set_gen()
#############################################
# Create a function that given a following two sets find the intersection
# and remove those elements from the first set.
# def intersect_del():
#     set1 = {65, 42, 78, 83, 23, 57, 29}
#     set2 = {67, 73, 43, 48, 83, 57, 29}
#
#     intersection = set1.intersection(set2)
#     for i in intersection:
#         set1.remove(i)
#     print(intersection)
#     print(set1)
#
#
# intersect_del()
#############################################
# Create a function that given two sets, Checks if One Set is Subset
# or superset of Another Set. if the subset is found delete all elements from that set
# def sup_sub():
#     first_set = {27, 43, 34}
#     second_set = {34, 93, 22, 27, 43, 53, 48}
#
#     print("First set is subset of second set - {}".format(first_set.issubset(second_set)))
#     print("Second set is subset of First set - {}".format(second_set.issubset(first_set)))
#     print()
#     print("First set is Super set of second set - {}".format(first_set.issuperset(second_set)))
#     print("Second set is Super set of First set - {}".format(second_set.issuperset(first_set)))
#     if first_set.issubset(second_set):
#         first_set.clear()
#     else:
#         second_set.clear()
#     print(first_set)
#     print(second_set)
#
#
# sup_sub()
########################################
# Create a function that Iterate a given list and Check if a given element already
# exists in a dictionary as a key’s value if not delete it from the list.
# def if_in_remove():
#     roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
#     sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#
#     for i in roll_number:
#         if i not in sample_dict.values():
#             roll_number.remove(i)
#
#     # roll_number = [item for item in roll_number if item in sample_dict.values()]
#     print(roll_number)
#
#
# if_in_remove()
#######################################
# Create a function that Given a dictionary get all values from the dictionary
# and add it in a list but don’t add duplicates.
# def no_duplicates():
#     speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#     unique = []
#     for i in speed.values():
#         if i not in unique:
#             unique.append(i)
#     print(unique)
#
#
# no_duplicates()
##########################################
# Create a function that remove duplicate from a list and create a tuple
# and find the minimum and maximum number.
# def rm_and_max_min():
#     sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#     sample_list = list(set(sample_list))
#     unique = tuple(sample_list)
#     print("Tuple: ", unique)
#     print("Max: ", max(unique))
#     print("Min: ", min(unique))
#
#
# rm_and_max_min()







