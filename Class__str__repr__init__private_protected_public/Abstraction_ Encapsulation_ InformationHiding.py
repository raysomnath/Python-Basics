# Encapsulation is seen as the bundling of data with the methods that operate on that data.
# Information hiding on the other hand is the principle that some internal information or data is "hidden",
# so that it can't be accidentally changed. Data encapsulation via methods doesn't necessarily mean that the data is hidden.
# You might be capable of accessing and seeing the data anyway, but using the methods is recommended.
# 
# Finally, data abstraction is present, if both data hiding and data encapsulation is used. This means data abstraction is the broader term: 
# 
# Data Abstraction = Data Encapsulation + Data Hiding 

# Encapsulation is often accomplished by providing two kinds of methods for attributes:
# The methods for retrieving or accessing the values of attributes are called getter methods.
# Getter methods do not change the values of attributes, they just return the values.
# The methods used for changing the values of attributes are called setter methods.

class Robot:
    
    def __init__(self, name= None, build_year=None):
        self.name = name
        self.build_year = build_year
    
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was build in "+ str(self.build_year))
        else:
            print("It's not known, when I was created!")
    
    # Setter methods
    def set_name(self, name):
        self.name = name
    
    def set_build_year(self, by):
        self.build_year = by

    # Getter methods
    def get_name(self):
        return self.name
    
    def get_build_year(self):
        return self.build_year

x = Robot()
x.set_name("Henry")
x.say_hi()
# >> Hi, I am Henry

y=Robot()
y.set_name(x.get_name())
print(y.get_name())
# >> Henry 

x = Robot("Henry", 2008)

y = Robot()

y.set_name("Marvin")

x.say_hi()
y.say_hi()

