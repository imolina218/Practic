# Reverse the following tuple.
# aTuple = (10, 20, 30, 40, 50)
# print(list(reversed(aTuple)))
##################################################
# Access value 20 from the following tuple.
# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# print(aTuple[1][1])
##################################################
# Create a tuple with single item 50.
# atuple = (50, )
# print(atuple)
##################################################
# Unpack the following tuple into 4 variables
# aTuple = (10, 20, 30, 40)
# a, b, c, d = aTuple
# print(a)
# print(b)
# print(c)
# print(d)
##################################################
# Swap the following two tuples.
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple1)
# print(tuple2)
##################################################
# Copy element 44 and 55 from the following tuple into a new tuple.
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:5]
# print(tuple2)
# print(tuple1)
##################################################
# Modify the first item (22) of a list inside a following tuple to 222.
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)
##################################################
# Sort a tuple of tuples by 2nd item.
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)
##################################################
# Counts the number of occurrences of item 50 from a tuple.
# tuple1 = (50, 10, 60, 70, 50)
# print(tuple1.count(50))
##################################################
# Check if all items in the following tuple are the same.


# def equal_in_tuple(x):
#     return all(i == x[0] for i in x)
#     # all returns a boolean value.
#
#
# tuple1 = (45, 45, 45, 45)
# print(equal_in_tuple(tuple1))


a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)





