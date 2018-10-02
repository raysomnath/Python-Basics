# To resule decorators we are importing the function defined 
# Decorators.py
import sys
from DecoratorsModuleWithArguments import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")

# Now both your say_whee() and greet("World") works