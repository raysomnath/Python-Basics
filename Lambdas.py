import sys

# A lambda funciton is small anonymous function
# A lambda function can take any number of arguments, but can have only expression
# lambda argurments : exprsssion
# The expressoin is executed and the result is returned

nums = [1,2,3,4,5,6]

def square(n):
    return n * n

print(list(map(square, nums)))

# Now let's do it by a lambda function
print(list(map(lambda n: n * n, nums)))
