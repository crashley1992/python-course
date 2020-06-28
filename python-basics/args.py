# args and kwargs means arguements and key word arguements

# a and b in this function are positional arguements
def myfunc(a,b):
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

myfunc(40,60)

# *args treats the arguements as a tuple, *args can be named whatever, just needs *. 
# Best naming convention is to use *args so others know what you mean
def nums(*args):
    return sum(args) * 0.05

result = nums(40,60,100,34)
print(result)

def mykwargs(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('No fruit here my dude')

mykwargs(fruit='apple', veggie='lettuce')


def myfunction(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunction(10,20,30, fruit='orange', food='eggs', animal='dog')