import sys
from DecoratorsWith_functools import do_twice

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

# without the @functools.wraps used in decorators file 
# say_whee.__name__ would have printed 'wrapper_do_twice' 
# but now it will not loose it's identity and preserve informaton about the original function.
print(say_whee.__name__)

# Technical Detail: The @functools.wraps decorator uses the function functools.update_wrapper()
# to update special attributes like __name__ and __doc__ that are used in the introspection.