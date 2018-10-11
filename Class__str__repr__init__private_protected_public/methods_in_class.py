# Methods in Python are essentially functions.

# Let's define a functon "hi", which takes object "obj" as an argument and assumes that this object has an attribute "name"

def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    pass

x = Robot() # instance creation
x.name = "Marvin" # adding an attribute "name" to the instance
hi(x) # calling the function hi and passing object x as an parameter to it.

#>>> Hi, I am Marvin! --> This will be be output of the above statement 

# Now, let's bind the "hi" function to a class attribute "say_hi"

class RobotWithClassAttribute:
    say_hi=hi

rwca = RobotWithClassAttribute()
rwca.name="Tuktuk"
RobotWithClassAttribute.say_hi(rwca)
#>>> Hi, I am Tuktuk! 

#"say_hi" is called a method. Usually, it will be called like this --> x.say_hi()
rwca.say_hi()
#>>> Hi, I am Tuktuk!

# Proper way to define methods in Python.
# 1. Instead of defining a function outside of a class definition and binding it to a class attribute,
#  we define a method directly inside (intended) of a class definition
# 2. The first parameter is used a reference to the calling instance.
# 3. This parameter is usually called self.  

# We have seen that a method differs from a function only in two aspects:
# It belongs to a class, and it is defined within a class
# The first parameter in the definition of a method has to be a reference to the instance,
# which called the method. This parameter is usually called "self".

# For a Class C, an instance x of C and a method m of C the following three method calls are equivalent:
# > type(x).m(x, ...)
# > C.m(x, ...)
# > x.m(...)