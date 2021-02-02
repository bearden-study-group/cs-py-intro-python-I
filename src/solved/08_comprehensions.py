"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

################################################################
# list-comprehension with numbers using range()
################################################################
# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

# LIST COMP using range() with two parameters `start=1, stop=6`
nums_1_thru_5 = [i for i in range(1, 6)]  # range(1, 6): start at 1, end at 5
print(f"nums_1_thru_5 {nums_1_thru_5}")

# Alternative LIST COMP to achieve the same result as above:
# using range() with one parameter `stop=5` (iterates through 0, 1, 2, 3, 4)
# and manipulating the variable called `i` directly
nums_1_thru_5_alt = [i + 1 for i in range(5)]  # range(5): start at 0, end at 4
print(f"nums_1_thru_5_alt {nums_1_thru_5_alt}")

# for-loop approach
# (NOTE: THIS IS NOT A COMPREHENSION, it just achieves the same result in a for-loop approach)
nums_1_thru_5_for_loop = []
for i in range(1, 6):
    nums_1_thru_5_for_loop.append(i)
print(f"nums_1_thru_5_for_loop {nums_1_thru_5_for_loop}")

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
cubes_0_thru_9 = [i ** 3 for i in range(10)]  # range(10) -> start at 0, end at 9
print(f"cubes_0_thru_9 {cubes_0_thru_9}")

################################################################
# list-comprehension with string manipulation
################################################################

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
words_arr = ["foo", "bar", "baz"]
upper_case_words = [word.upper() for word in words_arr]
print(f"upper_case_words = {upper_case_words}")

# for-loop approach
# (NOTE: THIS IS NOT A COMPREHENSION, it just achieves the same result in a for-loop approach)
upper_case_words_long = []
for word in words_arr:
    upper_case_words_long.append(word.upper())
print(f"upper_case_words_long = {upper_case_words}")

################################################################
# list-comprehension with `if` operator
################################################################

# Use a list comprehension to create a list containing only
# the _even_ elements the user entered into list x.
input_arr = input("Enter comma-separated numbers: ").split(',')

# note: must cast `num` to type int to use the modulo operator
# the comprehension below only selects elements in `input_arr` if the int value from the string is even
even_numbers = [num for num in input_arr if int(num) % 2 == 0]
print(f"even_numbers: {even_numbers}")

# for-loop approach
# (NOTE: THIS IS NOT A COMPREHENSION, it just achieves the same result in a for-loop approach)
even_nums_long = []
for num in input_arr:
    if int(num) % 2 == 0:
        even_nums_long.append(num)
print(f"even_nums_long: {even_nums_long}")
