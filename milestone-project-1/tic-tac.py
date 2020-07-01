# Player1 and Player Two assignments for X or O
def players():
    print('Player 1 choose if you want X or O')
    selected_input = input()
    while selected_input not in ['X', 'O']:
        print('Select either X or O')
        selected_input = input()

    player_one = selected_input
    if player_one == 'O':
        print('Player one is O')
        print('Player two is X')
        player_two = 'X'
    elif player_one  == 'X':
        print('Player one is X')
        print('Player two is O')
        player_two = 'O'
    
    return player_one, player_two

players()

# visual representation 
def display():
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    print(row1)
    print(row2)
    print(row3)

# Prompt if player is ready to play
def start_game():
    start_game == False
    print('Are you ready to start? Y or N')
    selected_input = input()
    if selected_input == "Y":
        start_game == True
        display()
# 
    while selected_input not in ['Y', 'N']:
            print('Select either Y or N')
            selected_input = input()

start_game()

# User input for selection for each move


# function for game

# check if tie, or win

# Updates after user input


