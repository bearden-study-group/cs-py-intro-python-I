"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
"""
list[index] — access element in list at location `index`
list[start:] — slice list from start (inclusive) ALL THE WAY TO END
list[:stop] — slice list from VERY BEGINNING to stop-1 (b/c stop is exclusive)
list[:] — slice list from VERY BEGINNING to THE VERY END (i.e., making a copy of the list)

list[start:stop:step] — slice list from index start (b/c start inclusive) to stop-1 (b/c stop is exclusive) by step
    list_02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice_02 = list_02[2:10:2]  # slice_02 = [2, 4, 6, 8]

"""

# QUICK TIP:
# if you ever need to reverse an array (or a string) without mutating the original iterable,
# you can use the following slice operation `[::-1]`
iter_to_reverse = [1, 2, 3, 4]
reversed = iter_to_reverse[::-1]
print(reversed)  # -> [4, 3, 2, 1]
print(iter_to_reverse)  # -> [1, 2, 3, 4]

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print("Output the second element: 4:")
print(a[1])

# Output the second-to-last element: 9
print("Output the second-to-last element: 9")
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print("Output the last three elements in the array: [7, 9, 6]")
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print("\n-------\n")
print("Output the two middle elements in the array: [1, 7]")
print(a[2:4])
print(a[2:-2])
print(a[-4:4])
print(a[-4:-2])
# EXTRA CREDIT: this would get two middle elements for any array
# don't worry about this for now, just tossed it in in case anyone is curious
print(a[(len(a) // 2) - 1:(len(a) // 2) + 1])

# Output every element except the first one: [4, 1, 7, 9, 6]
print("\n-------\n")
print("Output every element except the first one: [4, 1, 7, 9, 6]")
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print("\n-------\n")
print("Output every element except the last one: [2, 4, 1, 7, 9]")
print(a[:-1])

# For string s...

s = "Hello, world!"  # strings are ITERABLE!!! so slices apply to strings as well

#
print("\n-------\n")
print("Output just the 8th-12th characters: 'world'")
print(s[7:12])  # slice from index 7 to index 11 (b/c 12 is exclusive)
