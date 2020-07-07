# Errors and Exceptions Homework
# problem 1
for i in ['a','b','c']:
    try:
        result = i**2
        print(result)
    except:
        print('unsupported operand types')

# problem 2
x = 5
y = 0

z = x/y

try:
    print(z)
except ZeroDivisionError:
    print('Cant divide by zero')
finally:
    print('test done')

# Problem 3
def ask():
    while True:
        try:
            result = int(input('please provide a number'))
            result**0.5
        except:
            print('please input number')
        else:
            print('Square Root is: ')
            print( result**0.5)
            break
ask()
