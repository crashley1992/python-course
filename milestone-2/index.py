# normal deck should have 52
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# player places bet
class Player:
    def __init__(self, name, total):
        self.name = name
        self.total = total

    def place_bet(self):
        bet = input('Place Bet: ')
        print(bet)
    
    def __str__(self):
        return f'Player {self.name} has {self.total} to bet'

player_one = Player('Ashley', 100)
print(player_one)

# dealer has one card showing



# player cn choose to hit or stay 


# if the player is under 21 dealer then hits until they wither beat the player or the dealer busts

# human can bust by going over 21

# computer beats the dealer 

# computer busts


# face cards are worth 10

# aces can either be 1 or 11

