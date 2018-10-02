import sys

# Python alloows you to use decorators in a simpler way with the @symbol, sometimes called the "pie" syntax

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush, the neighbours are asleep
    return wrapper

@not_during_the_night
def say_whee():
    print("Whee!")

# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee).
# It’s how you apply a decorator to a function.

print(say_whee)
print(say_whee())