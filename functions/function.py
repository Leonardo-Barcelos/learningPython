"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result

"""

# Creating a Function
## In Python a function is defined using the def keyword

def my_function():
  print("Hello from a function")

print("-----------------------------------------------")

# Calling a Function
 
def my_function():
  print("Hello from a function")

my_function()

print("-----------------------------------------------")

# Arguments

"""
Information can be passed into functions as arguments.
Arguments are specified after the function name,
inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname).
When the function is called, we pass along a first name, which is used inside the function to print the full name:

"""
def my_function(fname):
  print(fname + " teste")

my_function("Learning")
my_function("Python")
my_function("Sadness")

print("-----------------------------------------------")

# Number of Arguments

"""
By default, a function must be called with the correct number of arguments.
  Meaning that if your function expects 2 arguments,you have to call the function with 2 arguments,
  not more, and not less

"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Lionel", "Messi")

print("-----------------------------------------------")

# Arbitrary Arguments, *args

"""
If you do not know how many arguments that will be passed into your function,
  add a * before the parameter name in the function definition.
"""
def my_function(*kids):
  print(kids)

my_function("Seiya", "Shiryu", "Hyoga", "Shun", "Ikki")

print("-----------------------------------------------")

# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function,
  add two asterisk: ** before the parameter name in the function definition.
"""
def my_function(**kid):
  print("His last name is " + kid['lname'])
  print("His last name is " + kid.get('lname')) # eu acho assim melhor porém precisa revisar

my_function(fname = "Bruce", lname = "Wayne", tteste= 'teste 0', ttest2 = "teste 1")