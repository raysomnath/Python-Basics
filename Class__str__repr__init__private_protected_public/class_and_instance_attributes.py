# Instance attributes are owned by the specific instances of a class.
# This means for two different instances the instance attributes are usually different

# Class attributes are attributes which are owned by the class itself.
# They will be shared by all the instances of the class.
# Therefore they have the same value for every instance.
# We define class attributes outside of all the methods, usually they are placed at the top, right below the class header.

# >>> class A:
# ...     a = "I am a class attribute"
# ...
# >>> x = A()
# >>> y = A()
# >>> x.a
# 'I am a class attribute'
# >>> y.a
# 'I am a class attribute'
# >>> A.a
# 'I am a class attribute'
# >>>

# If a class attribute needs to be changed, then it should be done with the notation ClassName.AttributeName.
# Otherwise, a new instance variable will be created.

# >>> class A():
# ...     a = "I am a class attribute!"
# ...
# >>> x = A()
# >>> y = A()
# >>> y.a
# 'I am a class attribute!'
# >>> x.a = "This creates a new instance attribute for x!"
# >>> A.a
# 'I am a class attribute!'
# >>> A.a = "This is changing the class attribute 'a'!"
# >>> A.a
# "This is changing the class attribute 'a'!"
# >>> y.a
# "This is changing the class attribute 'a'!"
# >>> # but x.a is still the previously created instance variable:
# ...
# >>> x.a
# 'This creates a new instance attribute for x!'
# >>>

# Python's class attribute and object attributes are stored in separate dictionaries, as we see here:
# >>> x.__dict
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'A' object has no attribute '__dict'
# >>> x.__dict__
# {'a': 'This creates a new instance attribute for x!'}
# >>> y.__dict__
# {}
# >>> A.__dict__
# mappingproxy({'__module__': '__main__', 'a': "This is changing the class attribute 'a'!", '__dict__': <attribute '__dict__' of 'A' objects>, 
# '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None})
# >>> x.__class__.__dict__
# mappingproxy({'__module__': '__main__', 'a': "This is changing the class attribute 'a'!", '__dict__': <attribute '__dict__' of 'A' objects>, 
# '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None})
# >>>