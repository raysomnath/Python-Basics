import sys
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwags):
        # Do something before
        value = func(*args, **kwags)
        # Do something after
        return value
    return wrapper_decorator