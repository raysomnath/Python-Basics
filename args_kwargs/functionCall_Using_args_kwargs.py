import sys

# Here we will call a function using *args and **kwargs. 
# Just consider that you have this little function:

def test_args_kwargs(arg1, arg2, arg3):
    print('arg1:',arg1)
    print('arg2:',arg2)
    print('arg3:',arg3)

# Now you can use *args or **kwargs to pass arguments to this little funciton. Here's how to do it:
args = ("two",3,5)
test_args_kwargs(*args)

# Now with **kwargs
kwargs = {"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)