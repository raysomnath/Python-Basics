import sys

num = [1,4,2,7,3,8,3,4,8,1]

print(sorted(num))

names = ['shaun', 'ryu', 'abe','Apple','Brian','shaun']
print(sorted(names))

print(set(num))
print(set(names))

def belt_count(dictionary):

    belts =list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)

        print(f'Threr are {num} {belt} belts')

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
        
belt_count(ninja_belts)