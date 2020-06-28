# Functions allow reusable blocks of code
# Use snake casing when naming funcitions ex: this_is_snake_casing
# and use CamelCase when creating classes

def name_of_function():
    print("hi")

# How to call the function
name_of_function()

# You can provide a default value so if there is no input, the function will still run
def say_hello(name="Default"):
    print(f'Hello {name}')

say_hello("Ashley")
say_hello()

def add_num(num1, num2):
    return num1+ num2

# return lets you save an output, so result can store the total of add_num function
result = add_num(10,20)
print(result)

# print vs return
def print_result(a,b):
    print(a + b)

print_result(10,30) #cant assign this to a variable

def return_result(a,b):
    return a + b

result = return_result(3,4) #returned result was assigned to variable
print(result)

def check_even_list(num_list):
    for number in num_list:
        if(number % 2 == 0):
            print("true")
            return True
        else:
            pass
    return False # ***Important to get correct indentation or else it will return false even when values are true

check_even_list([1,4,5])

# if you place false here w/o indentation it will only return the first false 
# value and not check if there are any other true value

def check_even_list2(num_list):
    # return all even numbers

    # place holder
    even_numbers = []

    for number in num_list:
        if(number % 2 == 0):
            even_numbers.append(number)
            print(even_numbers)
        else:
            pass

    return even_numbers #lined up with for loop 

#output [2,3]
check_even_list2([1,2,3,4,5])
            
stock_prices = [('APPLE', 200), ('GOOGLE', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

#handles price and ticker seperatly
for ticker, price in stock_prices:
    print(price + (0.1 * price))


work_hours = [('Abby', 100),('Billy', 400),('Cass', 800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #return tuple
    return (employee_of_month, current_max)

results = employee_check(work_hours)
# tuple unpacking
name,hours = employee_check(work_hours)
print(name)
print(hours)
print(results)

