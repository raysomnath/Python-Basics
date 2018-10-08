# The advantage of lambda operator can be seen when it used in 
# combination with the map() function

# map() is a function of two arguments:
# r = map(func, seq)

# The first argument func is the name of a function and the second a sequence (e.g. a list) seq.
# map applies the function func to all the elements of the sequence seq. It returns a new list with
# the elements changed by the func.
import sys

def fahrenheit(T):
    return ((float(9/5)*T+32))

def celsius(T):
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5, 39)

f = map(fahrenheit, temp)
for val in f:
    print(val)

c = map(celsius, temp)
for val in c:
    print(val)

# In the above example we have not used the lambda.
# By using lambda, we wouldn't have had to define and name the functions 
# fahrenheit() and celcius(). 

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print(Fahrenheit)

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print(C)

# map() can be applied to more than one list. The lists have to have the same length.
# map() will apply its lambda function to the elements of the argument lists, i.e. it first applies
# to the elements with the 0th index, then to the elements with the 1st index until the n-th index is reached: 
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
twoVariableSum = map(lambda x,y: x + y, a,b)
for val in twoVariableSum:
    print(val)

threeVariable = map(lambda x,y,z: x + y + z, a,b,c)
for val in threeVariable:
    print(val)

# We can see in the example above that the parameter x gets its values from the list a,
# while y gets its values from b and z from list c. 
