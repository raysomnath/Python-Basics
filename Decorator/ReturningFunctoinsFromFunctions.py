import sys

# Python also allows you to use functions as return values.\
# The following example returns one of the inner functions from the outer parent() function:

def parent(num):
    def first_child():
        return "Hi I am Emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

# Note that you are returning first_child without the parentheses.
# Recall that this means that you are returning a reference to the function first_child

first = parent(1)
second = parent(2)

print(first)
print(second)

# You can now use first and second as if they are regular functions,
# even though the functions they point to can’t be accessed directly:

print(first())
print(second())