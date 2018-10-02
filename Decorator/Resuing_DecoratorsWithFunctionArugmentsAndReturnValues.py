# To resule decorators we are importing the function defined 
# Decorators.py
import sys
from DecoratorsModuleWithArgumentsAndReturnValues import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

returnedValueFromWrapprerFunc = return_greeting("Somnath")
print(returnedValueFromWrapprerFunc)
