import sys

# It's possible to define functions inside other functions. Such functions are called inner functions.
# Here's an example of a funciton with two inner functions.

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")
    
    def second_child():
        print("Printing from the scond_child() function")
    
    second_child()
    first_child()

parent()

# Furthermore, the inner functions are not defined until the parent function is called.
# They are locally scoped to parent(): they only exist inside the parent() function as local variables.
# Try calling first_child(). You should get an error: