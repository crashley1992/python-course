# Class practice for using python to make a guessing game
# example = [1,2,3,4,5,6,7]

# import libary that has shuffle
from random import shuffle

def shuffle_list (mylist):
    shuffle(mylist)
    return mylist

# result = shuffle_list(example)
# print(result)

mylist = ['', 'O', '']

shuffle_list(mylist)

def player_guess():
    guess=''

    while guess not in ['0', '1', '2']:
        # input will always return a string so int() is needed to convert back to int
        guess = input("Pick a number: 0, 1, or 2:  ")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("correct")
    else:
        print("Wrong Guess!")
        print(mylist)
    
# Initial list
mylist = [' ', 'O', ' ']
# shuffle List
mixedup_list = shuffle_list(mylist)

# guess
guess = player_guess()

#checkguess
check_guess(mixedup_list, guess)