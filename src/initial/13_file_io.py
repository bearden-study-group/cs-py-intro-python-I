"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# print("--------OLD WAY")
# f = open("foo.txt")
# # print(f)
# read_file = f.read()
# print(read_file)
# print(f"f.closed ? {f.closed}")
# f.close()  # make sure you close the file
# print(f"f.closed ? {f.closed}")

print("\n--------NEW WAY")

with open("foo.txt") as f:
    # this level — local to with statement
    read_file = f.read()
    print(read_file)

print("FILE IS CLOSED")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# "w" overwrites everything in file
# "a" appends to end of file
# "x" creates file
# "r" is for reading file
with open("baz.txt", "w") as file_input:
    file_input.write("Arbitrary line 1\n")
    file_input.write("Arbitrary line 2\n")
    file_input.write("Arbitrary line 3\n")

with open("baz.txt", "r") as file_output:
    print("baz.txt after creation")
    print(file_output.read())
