# Dice rolling simulator
import random

def main():
    player1 = 0
    player2 = 0
    rounds = 1  #started at one so rounds wouldnt start at 0
    player1Wins = 0
    player2Wins = 0

    # Allows wounds to go till round 3
    # Game function that tracks dice rolls/wins
    while rounds != 4:
        print("Round " + str(rounds))
        print("Player1 has won " + str(player1Wins))
        print("Player2 has won " + str(player2Wins))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 rolls " + str(player1))
        print("Player 2 rolls " + str(player2))

        if player1 == player2:
            print("Draw\n")
        elif player1 > player2:
            player1Wins = player1Wins + 1
            print("Player 1 wins\n")
        else:
             player2Wins = player2Wins + 1
             print("Player 2 wins\n")

        rounds = rounds + 1

# function for random number
def dice_roll():
    dice_random = random.randint(1,6)
    return dice_random

main()    
