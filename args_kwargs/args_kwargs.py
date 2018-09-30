import sys

# *args and **kwargs are mostly used in function definitions. 
# *args and **kwargs allow you to pass a variable number of arguments to a function. 
# What variable means here is that you do not know beforehand how many arguments 
# can be passed to your function by the user so in this case you use these two keywords. 
# *args is used to send a non-keyworded variable length argument list to the function. 
# Here’s an example to help you get a clear idea:

def test_var_args(f_arg, *argv):
    print('first normal arg:',f_arg)
    for arg in argv:
        print('another arg through *argv:',arg)

test_var_args('yasoob','python','eggs','test')

# **kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function. 
# Here is an example to get you going with it

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key,value))

greet_me(name="yasoob")