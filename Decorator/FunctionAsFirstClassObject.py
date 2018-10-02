import sys

# In Python, functions are first-class objects.
# This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on).
# Consider the following three functions:

def say_hello(name):
    return f"Hello {name}"

def be_awsome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

# Here, say_hello