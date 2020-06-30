# user gets random word
# import libary that has shuffle
from random import shuffle

#holds words that the shuffle function will select from
words = ['maybe', 'stuff', 'cat']
# list that holds the selected word
word_to_guess = []
# list that holds letters from selected word
letters_to_guess = []
# holds letters correctly guess so user can see what's been displayed
correct_guesses = []
shuffle(words)

# function selects a random word from words array and appends each letter to letters_to_guess list
def word_select():
    selected_word = words[0]
    word_to_guess.append(selected_word)
    word = word_to_guess[0]
    for letter in word:
        letters_to_guess.append(letter)
        # print(letters_to_guess)

# function that tracks user input, conditionals for when guess matches letter, and params that keep the game going until won or lost
def game_play():
    word_select()
    total_gueses = 0
    while total_gueses < 10:
        guess = input()
        guess
        total_gueses += 1
        print(total_gueses)
        for letter in letters_to_guess:
            if guess == letter:
                print(letter + ' correct')
                correct_guesses.append(letter)
                print(correct_guesses)
                if len(correct_guesses) == len(letters_to_guess):
                    print('You Won!')
                    total_gueses = 10 #ends game loop
                    
game_play()

# improvements
# The letters guess dont appear in the correct order of the index for each guessed letter 
# for example stuff can be spelled utsff depening on order of correctly guessed letters
# add loss conditional to show what correct word was