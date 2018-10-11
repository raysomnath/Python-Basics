# There is no "real" destructor, but something similar, i.e. the method __del__.
# It is called when the instance is about to be destroyed and if there is no other reference to this instance.
# If a base class has a __del__() method, the derived class's __del__() method, if any,
# must explicitly call it to ensure proper deletion of the base class part of the instance. 
# The following script is an example with __init__ and __del__: 

class Robot():
    
    def __init__(self, name):
        print(name + " has been created!")
    
    def __del__(self):
        print("Robot has been destroyed")

if __name__ == "__main__":
    x = Robot("Tik-tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y

# The usage of the __del__method is very problematic.
# If we change the previous code to personalize the deletion of a robot, we create an error:
class RobotA():
    
    def __init__(self, name):
        print(name + " has been created!")
    
    def __del__(self):
        print(self.name + " says bye bye")

if __name__ == "__main__":
    x = RobotA("Tik-tok")
    y = RobotA("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
# Exception ignored in: <function RobotA.__del__ at 0x01231930>
# Traceback (most recent call last):
# destructor.py, line 33, in __del__
# print(self.name + " says bye bye")
# AttributeError: 'RobotA' object has no attribute 'name'
# Exception ignored in: <function RobotA.__del__ at 0x01231930>
# Traceback (most recent call last):
# destructor.py, line 33, in __del__
# print(self.name + " says bye bye")
# AttributeError: 'RobotA' object has no attribute 'name'