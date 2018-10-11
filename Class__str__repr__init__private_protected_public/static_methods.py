# We used class attributes as public attributes in the previous section. Of course, we can make public attributes private as well.
# We can do this by adding the double underscore again. If we do so, we need a possibility to access and change these private class attributes.
# We could use instance methods for this purpose: 

class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances(self):
        return Robot.__counter
        

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())

# This is not a good idea for two reasons: First of all, because the number of robots has nothing to do with a single robot
# instance and secondly because we can't inquire the number of robots before we haven't created an instance. 
# If we try to invoke the method with the class name Robot.RobotInstances(), we get an error message, because it needs an instance as an argument: 

# >>> Robot.RobotInstances()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: RobotInstances() takes exactly 1 argument (0 given)

# The next idea, which still doesn't solve our problem, consists in omitting the parameter "self": 

class RobotA:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    def RobotInstances():
        return Robot.__counter

# Now it's possible to access the method via the class name, but we can't call it via an instance: 

# >>> from static_methods2 import Robot
# >>> Robot.RobotInstances()
# 0
# >>> x = Robot()
# >>> x.RobotInstances()
# Traceback (most recent call last):

#   File "<stdin>", line 1, in <module>
# TypeError: RobotInstances() takes no arguments (1 given)
# >>> 

# The call "x.RobotInstances()" is treated as an instance method call and an instance method needs a reference to the instance as the first parameter. 

# So, what do we want? We want a method, which we can call via the class name or via the instance name without
# the necessity of passing a reference to an instance to it. 

# The solution consists in static methods, which don't need a reference to an instance. 
# It's easy to turn a method into a static method. All we have to do is to add a line with "@staticmethod" directly in front of the method header.
# It's the decorator syntax. 

# You can see in the following example that we can now use our method RobotInstances the way we wanted:

class RobotC:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1
    
    @staticmethod
    def RobotInstances():
        return RobotC.__counter

if __name__ == "__main__":
    print(RobotC.RobotInstances())
    x = RobotC()
    print(RobotC.RobotInstances())
    y = RobotC()
    print(x.RobotInstances())  
    print(RobotC.RobotInstances())