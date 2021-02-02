####################################
# GENERAL EXAMPLE
####################################
# This is a for-loop approach — NOTE: THIS IS NOT A COMPREHENSION
squared_nums_dict = {}
for num in range(1, 11):
    squared_nums_dict[num] = num * num
print(f"squared_nums_dict = {squared_nums_dict}")

# Here's the comprehension approach to the same problem above
squared_nums_comp = {num: num * num for num in range(1, 11)}
print(f"squared_nums_comp = {squared_nums_comp}")


####################################
# PROBLEM 1
# make a dictionary with key: value pairs such that
# each key is a number 0–9 (inclusive) and each value is the cube of that key
#
# GOAL: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
####################################
cubed_dict = {i: i ** 3 for i in range(10)}
print(f"cubed_dict = {cubed_dict}")  # -> {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}


####################################
# PROBLEM 2
# from the list `numbers`, construct a dictionary with key:value pairs such that every value is the result of squaring
# the key (value = key to the power of two). BUT only take the keys in numbers that are ODD
#
# GOAL: {473: 223729, 17: 289, 5: 25, 39: 1521, 1: 1}
####################################
numbers = [473, 20, 0, 17, 564, 5, 2, 39, 10, 1]
even_squared_nums = {i: i ** 2 for i in numbers if i % 2 != 0}
print(f"even_squared_nums = {even_squared_nums}")

####################################
# PROBLEM 3
# from the list `strings`, construct a dictionary with key:value entries where the key
# represents the index location (1-indexed instead of 0) of the string in the array
# and the value is the actual string
#
# GOAL: {1: 'land', 2: 'sea', 3: 'sky'}
####################################
strings = ["land", "sea", "sky"]
enumerated_dict = {i: j for i, j in enumerate(strings, 1)}
print(f"enumerated_dict = {enumerated_dict}") # -> {1: 'land', 2: 'sea', 3: 'sky'}

####################################
# PROBLEM 4
# given a nested list with two sub_lists (of equal length), construct a dictionary where the
# keys are the elements in the first sub_list and the
# values are the elements in the second sub_list
# note: the element order does matter
#
# GOAL:  {1: 'first', 2: 'second', 3: 'third'}
####################################
nested_list = [[1, 2, 3], ["first", "second", "third"]]
joined_dict = {i: j for i, j in zip(nested_list[0], nested_list[1])}
print(joined_dict)

####################################
# PROBLEM 5
# use a dictionary comprehension to create a dictionary with
# reversed key, value pairs from dict_to_flip
#
# In other words: inverse the dictionary dict_to_flip
#
# GOAL: inverse_dict = {10: "a", 20: "b", 30: "c"}
####################################
dict_to_flip = {"a": 10, "b": 20, "c": 30}

# inverse_dict = {10: "a", 20: "b", 30: "c"}
inverse_dict = {v: k for v, k in dict_to_flip.items()}
print(f"inverse_dict = {inverse_dict}")  # -> { 10: "a", 20: "b", 30: "c" }
