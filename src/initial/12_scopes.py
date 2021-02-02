# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

################################################################################
# PROBLEM 1
################################################################################
# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    x = 99


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(f"after invoking change_x: x = {x}")  # prints 12, but we WANT IT to print 99


################################################################################
# PROBLEM 2
################################################################################
# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(f"from outer: y = {y}")  # prints 120, but we WANT it to print 999


outer()

################################################################################
# PROBLEM 3
# this should be solved in a different way than above!!
################################################################################
def outer_two():
    y = 120

    def inner():
        y = 888

    inner()

    print(f"from outer_two: y = {y}")  # prints 120 but we WANT it to print 888


outer_two()


################################################################################
# PROBLEM 4
# closures exist in Python :) —— all the web people can be happy now
################################################################################
def closure_out(static_in):
    def closure_in(param):
        return static_in + param

    return closure_in


a = closure_out(1)
b = closure_out(100)

print(a(2))
print(b(2))
