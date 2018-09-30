import sys

# Python ha s an interesting feature called decorators to add functionality to an existing code.
# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time

# Everything in python are objets, Names that we define are simply identifiers boudn to these objects.
# Function are also object too (with attributs). Various different names can be boudn to the same function object
# Here is an example

def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello")

# When you run the code, both funcitons first and second gives same output. Here the names first and second refer to the same object.

# Functions can be passed as arguments to another function.
# Such function that take other functions as arguments are also called higher order functions.
# Here is an example of such a function

def inc(x) :
    return x + 1

def dec(x): 
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 3))
print(operate(dec, 3))

# Furthermore, a functoin can return another function.
# Here, is_returned() is a nested function which is defined and returned, each time we call is_called()
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

# Outputs "Hello"
new()

# Functions and methods are called callable as they can be called
# In fact, any object which implements the special method __call__() is termed callable.
# So, in hte most basic sene, a decorator is a callable that returns a callable

# Basicall, a decorator takes in a function, adds some functionality and returns it.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()

pretty = make_pretty(ordinary)
pretty()

# In the above example shown, make_pretty() is a decorator. In the assignment step.
# pretty = make_pretty(ordinary)
# We can see that the decorator function added some new functionality to the original funciton.
# This is similar to packing a gift. the decorator acts as a wrapper. The nature of the object
# that got decorated (action gift inside) does not alter. But now, it looks pretty (since it got decorated)

# Generally, we decorate a funciton and reassign it as,
# ordinary = make_pretty(ordinary)
# This is a common construct and for this reason, Python as a sytax to simplify this.
# We can use the @ symbol along with the name of the decortor function and place it above
# the difinition of the function to be decorated for example

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# is equivalent to
# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

# Decorating functions with parameters

# The above decorator was simple and it only worked with functions that did not have parameters. 
# What if we had functions that took parameters like below?
# def divide(a, b):
#    return a/b

# This funciton has two paramters, a and b. We know, it will give error if we pass b as 0
# >>> divide(2,5)
# 0.4
# >>> divide(2,0)
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero

# Now let's make a decorator to check for this case that will cause the error.
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b==0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(2,5))

print(divide(2,0))