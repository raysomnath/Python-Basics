import sys

# The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
# map(function, iterables)

from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))

# print(anagrams)

# Let's do it now by using map funcion
print(list(map(jumble, words)))

# in a comprehensive way
print([jumble(word) for word in words])
