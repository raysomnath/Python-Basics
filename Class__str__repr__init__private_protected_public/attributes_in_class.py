import sys

# Attributes and Properties are essentially differenet things in Python. Attributes explained here

# Attributes are created inside of a class definition
class Robot:
    pass

# Creating instance of Robot class
x = Robot()
y = Robot()

# We can dynamically create arbitrary new attributes for existing instances of a class.
# We do this by joining an arbitrary name to the instance name, separated by a dot ".".
# In the following example, we demonstrate this by created an attribute for the name and the build year:

x.name= "Marvin"        # This is not a proper way of creting attributes
x.build_year = "1979"   # This is not a proper way of creting attributes

y.name="Caliban"        # This is not a proper way of creting attributes 
y.build_year = "1993"   # This is not a proper way of creting attributes

print(x.name)
print(y.build_year)

print(x.__dict__)
#>>> {'name': 'Marvin', 'build_year': '1979'}

print(y.__dict__)
#>>> {'name': 'Caliban', 'build_year': '1993'}

# Attributes can be bound to class names as well. In this case, each instance will possess this name as well.

Robot.brand = "Kuka"

print(x.brand)
#>>> Kuka

x.brand = "Thales"
print(x.brand)
#>>> Thales

print(Robot.brand)
#>>> Kuka

print(y.brand)
#>>> Kuka

Robot.brand = "Thales"
print(x.brand)
#>>> Thales

print(y.brand)
#>>> Thales

print(x.__dict__)
#>>> {'name': 'Marvin', 'build_year': '1979', 'brand': 'Thales'}

print(y.__dict__)
#>>> {'name': 'Caliban', 'build_year': '1993'}

print(Robot.__dict__)
#>>> {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>, 
#     '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'brand': 'Thales'}

# If you try to access y.brand, Python checks first, if "brand" is a key of the y.__dict__ dictionary.
# If it is not, Python checks, if "brand" is a key of the Robot.__dict__. If so, the value can be retrieved. 

# If an attribute name is not included in either of the dictionary, the attribute name is not defined. If such an attribute is access then 
# AttributeError will raise. BUT by using getattr, this exception can be prevented, if an default value is provided as third argument

print(getattr(x,'energy',100)) #instance x do not have any attribute as energy...
#>>> 100

# Binding attributes to objects is a general concept in Python.
# Even function names can be attributed. You can bind an attribute to a function name in the same way, we have done so far to other instances of classes:

def f(x):
    return 42

f.x = 54
print(f.x)
#>>> 54
print(f(x))
#>>> 42
print(f)
#>>> <function f at 0x00C707C8>

# This can be used as a replacement for the static function variables of C and C++,
# which are not possible in Python. We use a counter attribute in the following example: 

def fg(x):
    fg.counter = getattr(fg, "counter", 0) + 1 
    return "Monty Python"
        

for i in range(10):
    fg(i)
    
print(fg.counter)
#>>> 10