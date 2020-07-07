# def add(n1,n2):
#     print(n1+n2)

# add(10,20 )

# number1 = 10

# number2 = input('Please Provide a number: ')

# add(number1,number2)

# try:
#     # attempt this code but may have error
#     result = 10 + 10
# except:
#     # What I want to happen when an error occurs
#     print('hey it looks like you arent adding correctly')
# else:
#     print('Add went well')
#     print(result)

# try:
#     f = open('testfile', 'w')
#     f.write("write a test line to file")
# except TypeError:
#     print("There was a type error")
# except OSError:
#     print("you have an OS error")
# finally: 
#     print('I always run' )


def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('end of try/except/finally')
            print('I will always run at the end')
        
ask_for_int()

