# There are two ways to restrict the access to class attributes:
# First, we can prefix an attribute name with a leading underscore "_".
# This marks the attribute as protected. It tells users of the class not to use this attribute unless, somebody writes a subclass
# Second, we can prefix an attribute name with two leading underscores "__". The attribute is now inaccessible and invisible from outside.
# It's neither possible to read nor write to those attributes except inside of the class definition itself.

#   Naming      Type            Meaning
#   name	    Public          These attributes can be freely used inside or outside of a class definition.
#   _name	    Protected       Protected attributes should not be used outside of the class definition, unless inside of a subclass definition. 
#   __name	    Private         This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, 
#                               except inside of the class definition itself.

class A:

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

# >>> from public_protected_private_attributes import A
# >>> x = A()
# >>> x.pub
# 'I am public'
# >>> x._prot
# 'I am protected'
# >>> x.__priv
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'A' object has no attribute '__priv'
# >>>

class Robot:

    def __init__(self, name=None,build_year=2000):
        self.__name = name
        self.__build_year = build_year
    
    def say_hi(self):
        if(self.__name):
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
    
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_build_year(self,by):
        self.__build_year = by
    
    def get_build_year(self):
        return self.__build_year
    
    def __repr__(self):
        return "Robot('"+ self.__name + "', " + str(self.get_build_year) + ")"

    def __str__(self):
        return "Name: "  + self.__name + ", Build Year: " + str(self.__build_year)

if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was build in the year " + str(rob.get_build_year()) + "!") 
    

