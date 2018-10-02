# To resule decorators we are importing the function defined 
# Decorators.py
import sys
from DecoratorsModule import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()