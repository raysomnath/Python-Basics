# Static methods shouldn't be confused with class methods.
# Like static methods class methods are not bound to instances,
# but unlike static methods class methods are bound to class.
# The first parameter of a class method is a reference to a class, i.e. a class object.
# They can be called via an instance of class name.

class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1
    
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())

class fraction(object):
    
    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)
    
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a , b = b, a%b
        return a
    
    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return(n1 // g, n2 // g)
    
    def __str__(self):
        return str((self.numerator)) + '/' + str(self.denominator)

# >>> from class_methods import fraction
# >>> x = fraction(8,24)
# >>> print(x)
# 1/3
# >>>

# We will demonstrate in our last example the usefulness of class methods in inheritance.
# We define a class "Pets" with a method "about".
# This class will be inherited in a subclass "Dogs" and "Cats".
# The method "about" will be inherited as well.
# We will define the method "about" as a "staticmethod" in our first implementation to show the disadvantage of this approach:

class Pets1:

    name = "pet animals"

    @staticmethod
    def about():
        print("This class is about {}!".format(Pets1.name))

class Dogs1(Pets1):
    name = "'man's best friends' (Frederick II)"

class Cats1(Pets1):
    name = "cats"
p = Pets1()
p.about()
d = Dogs1()
d.about()
c = Cats1()
c.about()

# This class is about pet animals!
# This class is about pet animals!
# This class is about pet animals!

# Especially, in the case of c.about() and d.about(), we would have preferred a more specific phrase!
# The "problem" is that the method "about" doesn't know that it has been called by an instance of the Dogs or Cats class. 
# We decorate it now with a classmethod decorator instead of a staticmethod decorator:

class Pets2:

    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))

class Dogs2(Pets2):
    name = "'man's best friends' (Frederick II)"

class Cats2(Pets2):
    name = "cats"

p = Pets2()
p.about()
d = Dogs2()
d.about()
c = Cats2()
c.about()

# This class is about pet animals!
# This class is about 'man's best friends' (Frederick II)!
# This class is about cats!