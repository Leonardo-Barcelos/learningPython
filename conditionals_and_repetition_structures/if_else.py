"""
Python relies on indentation (whitespace at the beginning of a line)
to define scope in the code.
Other programming languages often use curly-brackets for this purpose.

# to concat use %s <-- IMPORTANT
"""
x = 8000
y = 7999

print("-------------------------------------")

if x > y:
    print(f'Your power is over  {x} !!!!! %')
print("-------------------------------------")

if x > y:
    print(print(f"{x} is greater then {y}"))
elif x < y:  # The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
    print(print(f"{y} is greater then {x}"))
else:
    print("They are the same")

print("-------------------------------------")

# Short Hand If
if x > y:
    print(print(f"{y} is greater then {x}"))

# Short Hand If ... Else
print("X") if x > y else print("Y")
