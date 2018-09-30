import sys

# A very basic class would look like this

class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class")

# To assign the above class(template) to an object you would do the following
myobjectx = MyClass()

# Now the variable "myobjctx" holds an objec tof the class "MyClass" that contains the variable and the function defined within the class called "MyClass"
# To access the variable inside the of the newly created object "mybojctx" you would do the following
myobjectx.variable

# So for instance the below would print the string "blah"
print(myobjectx.variable)

# You can have multiple different objects that are of the same class.
# However, each object contains independent copies of the varialbe defined in the class.

myobjecty= MyClass()
myobjecty.variable = "yackiity"
print(myobjectx.variable)
print(myobjecty.variable)

# To acces a function inside of an object you use notaion similar to accessing a variable
myobjectx.function()

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())