import sys

# A dictionary is a data typ esimilar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, which is any type of object ( a string, a number, a list, etc.) instead of using its index to address it

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

print(phonebook)

# Alternately, a dictionary can be initialized with the same values in the following notation
phonebook2 = {
    "John" : 938477565,
    "Jack" : 938377269,
    "Jill" : 947662785
}

print(phonebook2)

# Dictionaries can be iterated over, just like a list. However, a dictionary, linke a list, does not keep the order
# of the values stored in it. To iterate over key value pairs, use the following syntax
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a specified index, use either one the following notations:

del phonebook2["John"]
print(phonebook2)

# or 
phonebook2.pop("Jill")
print(phonebook2)

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

#ninja_belts = {"crystal":"red","ryu":"black"}
#print(ninja_belts['crystal'])

#print('yoshi' in ninja_belts)

#print(ninja_belts.keys())
#print(list(ninja_belts.keys()))

#print(ninja_belts.values())
#print(list(ninja_belts.values()))

def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninj_belt = input('enter a belt color:')
    ninja_belts[ninja_name] = ninj_belt

    another = input('add another? y/n')
    if another == 'y':
        continue
    else:
        break
        
ninja_intro(ninja_belts)