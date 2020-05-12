# Below are the two lists convert it into the dictionary:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# result = dict(zip(keys, values))
# print(result)
############################################################
# Merge following two Python dictionaries into one:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# dict3 = dict1
# dict3.update(dict2)
# print(dict3)
############################################################
# Access the value of key ‘history’
# sampleDict = {
#    "class": {
#       "student": {
#          "name": "Mike",
#          "marks": {
#             "physics": 70,
#             "history": 80
#          }
#       }
#    }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])
############################################################
# Initialize dictionary with default values.
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# result_dict = dict.fromkeys(employees, defaults) # always create a new dictionary and never try to transform one
# print(result_dict)
############################################################
# Create a new dictionary by extracting the following keys from a
# given dictionary keys = ["name", "salary"]
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ["name", "salary"]
# new_dict = {i: sample_dict[i] for i in keys}
# print(new_dict)
############################################################
# Delete set of keys from Python Dictionary.
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# keysToRemove = ["name", "salary"]
# sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
# print(sampleDict)
############################################################
# Check if a value 200 exists in a dictionary
# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# print(200 in sampleDict.values())
############################################################
# Rename key city to location in the following dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New york"
# }
# sampleDict["location"] = sampleDict.pop("city")
# print(sampleDict)
############################################################
# Get the key corresponding to the minimum value from the following dictionary
# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sampleDict))
############################################################
# Given a Python dictionary, Change Brad’s salary to 8500.
sampleDict = {
     'emp1': {'name': 'John', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)





