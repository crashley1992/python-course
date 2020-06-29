# user gets random word
# import libary that has shuffle
from random import shuffle

words = ['maybe', 'stuff', 'because']
word_to_guess = []
letters_to_guess = []
shuffle(words)
# print(words)

def word_select():
    selected_word = words[0]
    word_to_guess.append(selected_word)
    word = word_to_guess[0]
    for letter in word:
        return letters_to_guess.append(letter)


def game_play():
    word_select()
    total_gueses = 0
    while total_gueses < 10:
        guess = input()
        guess
        total_gueses += 1
        print(total_gueses)
        for letter in letters_to_guess:
            if letter == guess:
                print('correct ' + letter + ' is in the word')
                

game_play()
