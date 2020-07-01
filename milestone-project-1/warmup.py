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
    # Varaible

    # inital 
    choice = 'WRONG'
    accetpable_range = range(0,10)
    within_range = False

    # Two Condirions to Check
    # Digit or WITHIN_RANGE IS ==FALSE
# isdigit keeps the loop going until the correct input is added
    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number(0-10): ')
         
        # DIGIT CHECK
        if choice.isdigit() == False:
            print('That is not a digit between 0 and 10.')

        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in accetpable_range:
                within_range = True
            else: 
                print('Pick between 0-10')
                within_range = False


    print(choice)
    return int(choice)

user_choice()

# result = 'WRONG VALUE'

# accetpable_values = [0,1,2]
# # output is false
# result in accetpable_values

# # output true
# result not in accetpable_values


game_list = [0,1,2]

def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input('Pick a position (0,1,2) :' )
        
        if choice not in ['0','1','2']:
            print('Sorry invalid choice! ')
        
        return int(choice)

def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at position: ')
    game_list[position] = user_placement

    return game_list

replacement_choice(game_list,1)


def game_on():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input('Keep playing? Y or N' )
        
        if choice not in ['Y','N']:
            print('Please choose Y or N  ')
        
        if choice == "Y":
            return True
        else: 
            return False

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = game_on()