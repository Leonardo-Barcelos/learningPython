
# IMPORTS
from operator import truediv

"""('EN-US')"""
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print('----------------------------------------------------')

"""('EN-US')"""
# Looping Through a String

for x in "banana":
    print(x)

print('----------------------------------------------------')

"""('EN-US')"""
# The break Statement


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print('----------------------------------------------------')

"""('EN-US')"""
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

print('----------------------------------------------------')

"""('EN-US')"""
# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('----------------------------------------------------')

"""('EN-US')"""
# The range() Function"
# To loop through a set of code a specified number of times, we can use the range() function,

for x in range(6):
    print(x)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5

print('----------------------------------------------------')

for x in range(2, 6):
    print(x)

print('----------------------------------------------------')

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print('----------------------------------------------------')

# The else block will NOT be executed if the loop is stopped by a break statement

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

print('----------------------------------------------------')

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print('----------------------------------------------------')

# The pass Statement
for x in [0, 1, 2]:
    pass
