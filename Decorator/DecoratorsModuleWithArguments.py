import sys

# *args and **kwargs in the inner wrapper function will accept an arbitrary number of positional and keyword arguments.

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
