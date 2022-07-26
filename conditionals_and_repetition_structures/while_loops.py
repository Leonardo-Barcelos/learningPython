# With the while loop we can execute a set of statements as long as a condition is true.

from curses import A_ALTCHARSET
from re import A


i = 1
while i < 6:
    print(i)
    i += 1
print("---------------------------------------------")

# The break Statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break

    i += 1
print("---------------------------------------------")

# The continue Statement

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("---------------------------------------------")


# The else Statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
