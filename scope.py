import sys

my_global = 'somnath'

def my_function():
    global my_global
    my_global = 'ray'
    print('inside the function the value of my_global is', my_global)

my_function()
print('outside the function the value of my_global is', my_global)