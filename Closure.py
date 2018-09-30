import sys

# Before getting into what a closure is, we have to first understand what a nested function 
# and nonlocal variable is.
# A function defined inside another function is called a nested function. Nested functions 
# can access variables of the enclosing scope
# In Python, these non-local variables are read only by default and we must declare them
# explicitly as non-local (using nonlocal keyword) in order to modify them.
# Following is an example of a nested function accessing a non-local variable

def print_msg(msg):
    # This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    
    # We can see that the nested function printer() was able to access the non-local 
    # variable msg of the enclosing function
    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

# In the example above, what would happen if the last line of the function print_msg()
# returned the printer() function instead of calling it. This means the function was defined as follows

def modifiedPrint_msg(msg):
    # This is the outer enclosing function
    def modified_Printer():
        #This is the nested function
        print(msg)
    
    return modified_Printer #this got changed

# Now let's try calling this function.
# OUtput: Hello
another = modifiedPrint_msg("Hello")
another()

# That's unusal.
# The modifiedPrint_msg() function was called with the string "Hello" and the returned 
# function was bound to the name another. On calling another(), the message was still
# remembered although we had already finished executing the modifiedPrint_msg() function

# This technique by which some data ("Hello") gets attached to the code is called closure in Python
# This value in te enclosing scope is rememebered when the variable goes out of scope 
# or the function itself is removed from the current namespace


# When do we have a closure?
# The criteria that must be met to create closure in Python are summarized in the following points
# > We must have a nested fucntion (funciton inside a function)
# > The nested fucntion must refer to a value defined in the enclosing funciton.
# > The enclosing funciton must return the nested function

# When to use closures?
# Closures can avoid the use of global values and provides some form of data hiding.
# It can also provide an object oriented solution the problem.
# When ther are few methods (one method in most cases) to be implemented in a a class,
# closures can provide an alternate and more elegant solutoin. But when the number of 
# attributes and methods gets larger, better implement a class.

# Here is a simple example where a closure might be more prefereable than defining a class
# and making objects.

def make_multiplier_of(n):
    def multipliler(x):
        return x * n
    return multipliler

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Ouput : 15
print(times5(3))

# Output : 30
print(times5(times3(2)))

# On a concluding note, it is good to point out that the values that get enclosed in the 
# closure function can be found out.

# All function objects have __closure__ attribute that returns a tuple of cell objects
# if it is a closure function. Referring to the example above, we know time3 and times5
# are closure funcitons.    