# Add a list of elements to a given set.
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list_add = ["Blue", "Green", "Red"]
# set.update(sample_set, sample_list_add)
# print(sample_set)
############################################################
# Return a set of identical items from a given two Python set.
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# print(set1.intersection(set2))
############################################################
# Returns a new set with all items from both sets by removing duplicates.
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1.union(set2)
# print(set3)
############################################################
# Given two Python sets, update first set with items that exist only
# in the first set and not in the second set.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)
############################################################
# Remove 10, 20, 30 elements from a following set at once.
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)
############################################################
# Return a set of all elements in either A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2):
#     print("The two set have no items in common.")
# else:
#     print("The two sets have items in common.")
#     print(set1.intersection(set2))
#     print("The different items that they have are:")
#     print(set1.symmetric_difference(set2))
############################################################
# Update set1 by adding items from set2, except common items.
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)
############################################################
# Remove items from set1 that are not common to both set1 and set2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.intersection_update(set2)
# print(set1)











