# user gets random word
# import libary that has shuffle
from random import shuffle

words = ['maybe', 'stuff', 'cat']
word_to_guess = []
letters_to_guess = []
correct_guesses = []
shuffle(words)

def word_select():
    selected_word = words[0]
    word_to_guess.append(selected_word)
    word = word_to_guess[0]
    for letter in word:
        letters_to_guess.append(letter)
        # print(letters_to_guess)


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
