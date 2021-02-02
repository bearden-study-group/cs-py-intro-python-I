# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# TODO: For the following challenges, DO NOT USE AN ASSIGNMENT (=).


###############################
# Problem 1
# Change x so that it is [1, 2, 3, 4]
###############################
# YOUR CODE HERE
x.append(4)
print("\nPROBLEM 1")
print(f"after x.append(4) -> x={x}")

###############################
# Problem 2
# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
###############################
# YOUR CODE HERE
x.extend(y)
print("\nPROBLEM 2")
print(f"after x.extend(y) -> x={x}")

# /////////////////////////////////
# QUICK NOTE ON EXTEND VS APPEND
# /////////////////////////////////
# List.extend(Iterable) will add every element from the iterable passed in to the list calling .extend()
# for example:
print("\nQUICK NOTE ON EXTEND VS APPEND")
list_to_extend = ["foo", "bar", "baz"]
list_to_extend.extend(["zab", "rab", "oof"])
print(f"using .extend() -> {list_to_extend}")  # -> Prints ["foo", "bar", "baz", "zab", "rab", "oof"]

# why USE extend?? let's look at what happens with .append() in the same situation:
list_to_append = ["foo", "bar", "baz"]
list_to_append.append(["zab", "rab", "oof"])
print(f"using .append() -> {list_to_append}")  # -> Prints ["foo", "bar", "baz", ["zab", "rab", "oof"] ]
# so if you append list_b into list_a, Python assumes you want list_b to fill ONE ELEMENT SLOT within list_a

# NOTE adding arrays with the + operator ALSO EXTENDS!!!
list_addend_01 = ["foo", "bar", "baz"]
list_addend_02 = ["zab", "rab", "oof"]
list_sum = list_addend_01 + list_addend_02
print(f"extend using + operator -> {list_sum}")
# or
list_addend_01 += list_addend_02
print(f"extend using += operator -> {list_sum}")


###############################
# Problem 3
# x is currently [1, 2, 3, 4, 8, 9, 10]
# Change x so that it is [1, 2, 3, 4, 9, 10]
###############################
# YOUR CODE HERE
print("\nPROBLEM 3")
x.remove(8)  # removes the element with a value of `8` in list `x`; returns `None`
print(f"after x.remove(8) -> x={x}")  # should print [1, 2, 3, 4, 9, 10]


# //////////////////////////////////
# ALTERNATIVE WAYS TO DO PROBLEM 3:
# //////////////////////////////////
# IF YOU KNEW THE INDEX YOU WANTED TO DELETE
# removed = x.pop(-3)  # element 8 is at the second-to-last index; pop at index -3 will remove that element and return the removed value
# removed = x.pop(4) # element 8 is at the 4th index; pop at index 4 will remove that element and return the removed value
# print(removed)  # -> would print 8

# IF YOU DIDN'T KNOW ABOUT .remove()
# please don't do this in the wild, I'm just trying to show you a range of List methods.
# removed = x.pop(x.index(8))  # this will find the index of element 8 and then pop at that index
# print(removed)  # -> would print 8


###############################
# Problem 4
# x is currently [1, 2, 3, 4, 9, 10]
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
###############################
# YOUR CODE HERE
x.insert(-1, 99)  # insert value 99 before index -1.
print(f"after x.insert(-1, 99) -> x={x}")


###############################
# Problem 5
# x is currently [1, 2, 3, 4, 9, 99, 10]
# Print the length of list x (should output 7)
###############################
# YOUR CODE HERE
print(f"len(x)={len(x)}")


###############################
# PROBLEM 6
# Print all the values in x multiplied by 1000
###############################
# YOUR CODE HERE
# option 1
for num in x:
    print(num * 1000)
# option 2
for i in range(len(x)):
    print(x[i] * 1000)
# option 3
print([num * 1000 for num in x])
