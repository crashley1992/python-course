# Import random library
import random

# playing game status set to true to start the game
playing = True

# normal deck should have 52
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# creates card objects that will be in deck
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

# player places bet, function lets you assign a name and starting money for bets
class Player:
    def __init__(self, name, total):
        self.name = name
        self.total = total
    
    def __str__(self):
        return f'Player {self.name} has {self.total} to bet'

player_one = Player('Ashley', 100)

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # pushes card object to empty list
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: " + deck_comp

    # shuffles empty deck list that Card object was appended to
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card       

#  test to make sure deck is printing and shuffles correctly
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

# what cards are dealt to each player
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # card passed in is from the Deck object Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank] 
        # track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):

        # if the total value is over 21 the ace value will be 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()
# player
test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(test_deck.deal())
print(test_player.value)


class Chips:
    
    def __init__(self, total=100):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Input an integer.')
        else: 
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {} '.format(chips.total))
            else:
                break
    
def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print('Player stands dealers turn')
            playing = False
        else:
            print('Enter h or s')
            continue
        break


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


def player_busts(player,dealer,chips):
    print("Bust Player")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player Wins')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player wins. Dealer busted')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Dealer wins. Player busted')
    chips.lose_bet()
    
def push(player,dealer,chips):
    print('dealer and player tie. Push')


while True:
    # Print an opening statement
    print('Welcome to Blackjack')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    # Create & shuffle the deck, deal two cards to each player
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        hit_or_stand(deck,player_hand)
        # Prompt for Player to Hit or Stand
        show_some(player_hand,dealer_hand)
        
        # Show cards (but keep one dealer card hidden)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)        

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value < 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
 # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break