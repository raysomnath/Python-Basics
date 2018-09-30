import sys

#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name
def my_function():
    print("Hello From My Function!")

my_function()

#unctions may also receive arguments (variables passed from the caller to the function). For example:
def my_funcion_with_args(username, greetings):
    print("Hello, %s, from my Function!, I wish you %s" %(username, greetings))

my_funcion_with_args("somnath", "good night")

#Functions may return a value to the caller, using the keyword- 'return' . For example:
def sum_two_numbers(a,b):
    return a + b

print("The sum of two numbers 2 & 3  = %d" %sum_two_numbers(2,3))

#Test
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()