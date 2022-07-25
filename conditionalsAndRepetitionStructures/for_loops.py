
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('--------------------------------------------------')  
  
# Looping Through a String

for x in "banana":
  print(x)
print('--------------------------------------------------')
    
# The break Statement

## Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print('--------------------------------------------------')
  
## Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
    