import sys

age = int(input('Enter your age:'))

if age < 10:
    # code block
    print('you are young, strange one')
elif age < 40:
    print('the fire in you is strong, strange one')
else:
    print('you are wise beyond doubt, strange one')


meaty = input('Do you want meat? (y/n)')

if meaty == 'y':
    print('here is the meaty menu... ')
else:
    print('here is the veggie menu...')

