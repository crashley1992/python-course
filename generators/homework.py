# Problem 1
def gensquares(N):
    for x in range(N):
        yield x**2


for x in gensquares(10):
    print(x)

# Problem 2
import random

random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

# problem 3
s = 'hello'

s_iter = iter(s)
print(next(s_iter))

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
# Generator functions allow you to declare a function that behaves like an iterator.
# doesnt use up more memory than needed

# Extra Credit!
# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


# If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator.


for n in range(101):
    if n % 2 == 0 and n in range(2,6):
        print(f'Not Weird {n}')
    if n % 2 == 0 and n in range(6,21):
        print(f'Weird {n}')
    elif n % 2 == 0 and n > 20: 
        print(f'Not Weird {n}')
    else:
        print(f'Weird {n}')
        

