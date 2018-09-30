import sys
num1 = 3.1425467389
num2 = 10.2903948

print('num 1 is', num1 , 'amd num2 is', num2)

# Format method
print('num 1 is {0} and num 2 is {1}'.format(num1, num2))
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))

# Using F-Strings
print(f'num 1 is {num1} and num 2 is {num2}')
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')