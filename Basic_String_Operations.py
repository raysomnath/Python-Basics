import sys

astring = "Hello world!"
astrting2 = 'Hellow world!'

print ("Single quotes are ' '")

print(len(astring))

print (astring.index("o"))
print (astring.count("l"))
print (astring[3:7])
print (astring[3])
print (astring[3:])
print (astring[:7])
print (astring[-3])

#This prints the characters of string from 3 to 7 skipping one character.
#This is extended slice syntax. The general form is [start:stop:step].
print (astring[3:7:1])

#There is no function like strrev in C to reverse a string.
#But with the above mentioned type of slice syntax you can easily
#reverse a string like this
print (astring[::-1])

print (astring.upper())
print (astring.lower())

#his is used to determine whether the string starts with something or ends with something, respectively.
#The first one will print True, as the string starts with "Hello".
#The second one will print False, as the string certainly does not end with "asdfasdfasdf".
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print (afewwords)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
