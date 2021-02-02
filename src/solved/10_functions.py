# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


# Return "Even!" if the number is even. Otherwise return "Odd"

# YOUR CODE HERE
def is_even_short(number):
    print("Even!" if number % 2 == 0 else "Odd")


def is_even_long(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd")


is_even_short(num)
is_even_long(num)
