# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    global x
    x = 99
    # print(x)


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()


def outer_two():
    outer_two.y = 120

    def inner():
        outer_two.y = 888
        print(outer_two.y)

    inner()

    print(outer_two.y)


outer_two()


def closure_out(static_in):
    def closure_in(param):
        return static_in + param

    return closure_in


a = closure_out(1)
b = closure_out(100)

print(a(2))
print(b(2))
