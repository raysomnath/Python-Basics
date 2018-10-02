# To resue a decorator we have moved the decorator to it's own module

import sys

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
