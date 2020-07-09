# def func():
#     return 1

# def hello():
#     return 'Hello'
# # greet will still point to hello object even after being deleted
# greet = hello

# # output Hello
# greet()


# def hello(name='ashley'):
#     print('hello func executed')

#     def greet():
#         return '\t This is the greet func inside hello'

#     def welcome():
#         return '\t This is the welcome func inside hello'

#     print('I am returning')

#     if name == 'Jose':
#         return greet
#     else: 
#         return welcome

# my_new_fun = hello('Jose')
# print(my_new_fun())
# hello()

def cool():
    def super_cool():
        return 'I am so cool'

    return super_cool

some_func = cool()
print(some_func())


def hello():
    return 'Hi Jose'

def other(some_def_func):
    print('Other code yo')
    print(some_def_func())

other(hello)



def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before original function')

        original_func()
        print('Some extra code after the original function')

    return wrap_func 

# def func_needs_decortor():
#     print('I want to be decorated!!')

# decorated_func = new_decorator(func_needs_decortor())


@new_decorator
def func_needs_decortor():
    print('I want to be decorated!!')