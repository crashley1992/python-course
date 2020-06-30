# Practice for project 1 

# Displaying information
# print([1,2,3])

# print([1,2,3])
# print([4,5,6])
# print([7,8,9])

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1,row2,row3):
    row2[1] = 'X'

    print(row1)
    print(row2)
    print(row3)
    

display(row1, row2, row3)

result = input('Please enter a value: ') #input returns a string
result_int = int(result)
print(result_int)

position_index = int(input("Choose an index position: "))
row2[position_index]

# Validate user input
def user_choice():
    choice = input('Please enter a number(0-10): ')
    print(choice)
    return int(choice)

user_choice()