# We can depict various data as string by using the str function, which uses "magically" the internal __str__ method of the corresponding data type.
# __repr__is similar. It also produces a string representation. 

# >>> l = ["Python", "Java", "C++", "Perl"]
# >>> print(l)
# "['Python', 'Java', 'C++', 'Perl']"
# >>> repr(l)
# "['Python', 'Java', 'C++', 'Perl']"
# >>> d = {"a":3497, "b":8011, "c":8300}
# >>> print(d)
# {'a': 3497, 'c': 8300, 'b': 8011}
# >>> str(d)
# "{'a': 3497, 'c': 8300, 'b': 8011}"
# >>> repr(d)
# "{'a': 3497, 'c': 8300, 'b': 8011}"
# >>> x = 587.78
# >>> str(x)
# '587.78'
# >>> repr(x)
# '587.78'
# >>> 

# If you apply str or repr to an object, Python is looking for a corresponding method __str__ or __repr__ in the class definition of the object.
# If the method does exist, it will be called.
# In the following example, we define a class A, having neither a __str__ nor a __repr__ method.

class A:
    pass

a = A()

print(a)
# >> <__main__.A object at 0x02E6CC90>

print(str(a))
# >> <__main__.A object at 0x02E6CC90>

print(repr(a))
# >> <__main__.A object at 0x02E6CC90>

# As both methods are not available, Python uses the default output for our object "a". 

# If a class has a __str__ method, the method will be used for an instance of x of that class, if either
# the function str is applied t oit or if it used in a print function.
# __str__ will not be used if __rerp__ is called, or if we try to ouput the value directly in an interactive Python shell

# >>> class B:
# ...     def __str__(self):
# ...             return "42"
# ...
# >>> b = B()
# >>> print(repr(b))
# <__main__.B object at 0x0000004CEF56D940>
# >>> print(str(b))
# 42
# >>> b
# <__main__.B object at 0x0000004CEF56D940>
# >>> print(b)
# 42

# We can see that eval(repr_s) returns again a datetime.datetime object.
# The String created by str can't be turned into a datetime.datetime object by parsing it. 

# >>> import datetime
# >>> today = datetime.datetime.now()
# >>> today
# datetime.datetime(2018, 10, 11, 19, 24, 9, 608265)

# >>> str_s = str(today)
# >>> str_s
# '2018-10-11 19:24:09.608265'
# >>> eval(str_s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<string>", line 1
#     2018-10-11 19:24:09.608265
#                 ^
# SyntaxError: invalid syntax

# >>> repr_s = repr(today)
# >>> t = eval(repr_s)
# >>> t
# datetime.datetime(2018, 10, 11, 19, 24, 9, 608265)
# >>> type(t)
# <class 'datetime.datetime'>
# >>>

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    
    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"
    
    def __str__(self):
         return "Name: " + self.name + ", Build Year: " + str(self.build_year)
    
if __name__ == "__main__":
    x = Robot("Marvin", 1979)

    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))

    #new = eval(x_str)
    #print(new)
    #print("Type of new: ", type(new))

    #   Traceback (most recent call last):
    #   File "__str__ and __repr__Methods.py", line 105, in <module>
    #   new = eval(x_str)
    #   File "<string>", line 1
    #   Name: Marvin, Build Year: 1979

    

    # x_repr can still be turned into a Robot object: 
    x_repr = repr(x)
    print(x_repr,type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new: ", type(new))

    # Robot('Marvin', 1979) <class 'str'>
    # Name: Marvin, Build Year: 1979
    # Type of new:  <class '__main__.Robot'>