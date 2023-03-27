#define function that returns a value
def add(x, y):
    result = x + y
    return result

#read a and b from user
a = float(input('Enter a : '))
b = float(input('Enter b : '))

#compute a + b
output = add(a, b)
print(f'Output  : {output}')


#function that returns multiple values
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

#read a and b from user
a = int(input('Enter a : '))
b = int(input('Enter b : '))
print(f'\nBefore Swap - (a, b)  : ({a}, {b})')
#swap a, b
a, b = swap(a, b)
print(f'\nAfter  Swap - (a, b)  : ({a}, {b})')