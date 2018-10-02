import sys

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# The so-called decoration happens at the following line:
say_whee = my_decorator(say_whee)
# In effect, the name say_whee now points to the wrapper() inner function. 
# However, wrapper() has a reference to the original say_whee() as func, 
# and calls that function between the two calls to print().

# Put simply: decorators wrap a function, modifying its behavior.