# Lambda Expressions - create anonymous functions
def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

list(map(square,my_nums))

# Output ['EVEN', 'E', 'S']
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else: 
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

test = list(map(splicer, names))
print(test)

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

list(filter(check_even,mynums))

for n in filter(check_even, mynums):
    print(n)

# lambda example
lambda num: print(num ** 2)

list(map(lambda num:num**2, mynums))


list(filter(lambda num: num %2 == 0))

list(map(lambda x:x[0],names))