import sys

# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# filter(function, iterable)

grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails, grades)))

filterd_grades = []

for grade in grades:
    if grade != 'F':
        filterd_grades.append(grade)
print(filterd_grades)

print([grade for grade in grades if grade != 'F'])