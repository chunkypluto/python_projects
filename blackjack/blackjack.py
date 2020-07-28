#! /usr/bin/python
# This is the main script for the blackjack game.
# Game Play:
# To play a hand of Blackjack the following steps must be followed:
# Create a deck of 52 cards
# Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player's bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer's cards, the other remains hidden
# Show both of the Player's cards
# Ask the Player if they wish to Hit, and take another card
# If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# If a Player Stands, play the Dealer's hand. The dealer will always Hit 
# until the Dealer's value meets or exceeds 17
# Determine the winner and adjust the Player's chips accordingly
# Ask the Player if they'd like to play again

# each deck has 4 suits, hearts, diamonds, clubs, spades
# each suit has 13 cards
# jacks, queens, kings have a value of 10
# aces have a value of 11 or 1

import random, time

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', \
    'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, \
    'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    '''
    Each Card object has a suit and a rank
    '''
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits

    def __str__(self):
        return f'{self.ranks} of {self.suits}'

class Deck():
    '''
    Each Deck object has 52 Card objects
    '''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
   #    deck_comp = ''
   #    for card in self.deck:
   #        deck_comp += '\n' + card.__str__()
        # return deck_comp
        for card in self.deck:
            print(f'{card.ranks} of {card.suits}')
        return "That's the deck!"

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    # deal the top Card from the Deck first
    def deal(self):
        return self.deck.pop()

class Hand():
    '''
    Each Hand object holds those Cards that have been dealt
    '''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # add card's value, check for aces and add them up since there 4 of them
    def add_card(self,card):
        # card passed in from Deck.deal(), which is a single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.ranks]
        if card.ranks == 'Ace':
            self.aces += 1

    # ajust an Ace's value from 11 to 1
    def adjust_for_aces(self):
        self.value -= 10

class Chips():
    '''
    Chips for player
    '''
    def __init__(self):
        self.total = 100
        self.bet = 0
        # print(f"Player Chips: {self.total}\n")

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __str__(self):
        return f"Player Chips: {self.total}\n"

def take_bet(chips):
    '''
    Ask for a player's bet as an integer value. Try to use try/except.
    Check for available Chips and see if the bet is covered.
    '''
    while True:
        try:
            chips.bet = int(input("Place a bet: "))
        except:
            print('Invalid value')
            continue
        if chips.bet > chips.total:
            print(f'Sorry insuffient chips. Available chips: {chips.total}')
        else:
            print('Your bet has been accepted.')
            break

def hit(deck, hand):
    '''
    Take hits until bust. This function will be called during gameplay anytime a Player
    requests a hit, or a Dealer's Hand is less than 17.
    It should take in Deck and Hand objects as arguements, and deal one card off the deck
    and add it to the hand. Check for aces in the event the Hand exceeds 21
    '''
    onecard = deck.deal()
    hand.add_card(onecard)
    # adjust for aces if value greater than 21
    # will check every time there's an ace
    if hand.value > 21 and hand.aces > 0:
        hand.adjust_for_aces()

    print(f"Card dealt: {onecard}")
    # return hand


def hit_or_stand(deck, hand):
    '''
    This function accepts the Deck and Hand as arguements, 
    and assign playing as a global variable for controlling a while loop during gameplay.
    If the Player Hits, use hit() function. If the Player stands, set the playing False
    '''
    global playing 
    action = ' '
    while action != 'h' and action != 's':
        action = input('Player, hit or stand (h/s): ').lower()
    if action == 'h':
        hit(deck, hand)
        show_some(playerhand, dealerhand)
        playing = True
    else:
        print("Stand. Dealer's turn.")
        playing = False

        
def show_some(player, dealer):
    '''
    Show all of player's Hand, and make first card of dealer visible
    '''
    print("\n"+20*"-")
    print("Player's hand: ")
    for index, card in enumerate(player.cards):
        print(f"#{index+1}. {card}")

    print("\nDealer's hand: ")
    print(f"#1. {dealer.cards[0]}")
    for index, card in enumerate(dealer.cards[1:]):
        print(f"#{index+2}. [Card hidden]")
    print(20*"-"+"\n")

def show_all(player, dealer):
    '''
    Show all Hands
    '''
    print("\n"+20*"-")
    print("Player's hand: ")
    for index, card in enumerate(player.cards):
        print(f"#{index+1}. {card}")

    print("\nDealer's hand: ")
    for index, card in enumerate(dealer.cards):
        print(f"#{index+1}. {card}")
    print(20*"-"+"\n")

def player_busts(playerhand, playerchips):
    print(f"Player busted! {playerhand.value}")
    print(f"Dealer wins! {dealerhand.value}")
    playerchips.lose_bet()
    print(f"Player loses a bet of {playerchips.bet}")

def player_wins(dealerhand, playerhand, playerchips):
    print(f"Player wins! {playerhand.value}")
    print(f"Dealer loses! {dealerhand.value}")
    playerchips.win_bet()
    print(f"Player wins a bet of {playerchips.bet}")

def dealer_busts(dealerhand, playerchips):
    print(f"Dealer busted! {dealerhand.value}")
    print(f"Player wins! {playerhand.value}")
    playerchips.win_bet()
    print(f"Player wins a bet of {playerchips.bet}")

def dealer_wins(dealerhand, playerhand, playerchips):
    print(f"Dealer wins! {dealerhand.value}")
    print(f"Player loses! {playerhand.value}")
    playerchips.lose_bet()
    print(f"Player loses a bet of {playerchips.bet}")

def push(dealerhand, playerhand):
    print(f"Tie game! Player: {playerhand.value} Dealer: {dealerhand.value}")

# to be expanded
# format cards to display nicely
def printcard(card):
    clist = card.split()
    return clist

def playagain():
    ans = input("Play again? y/n: " ).lower()
    return ans == 'y'

# main
if __name__ == '__main__':
    
    # declare a Chip object outside of while loop to keep track of bets
    playerchips = Chips()

    while True:
        # opening statement
        print("Welcome to Blackjack!\n")

        # create & shuffle the deck
        pdeck = Deck()
        pdeck.shuffle()
        
        # print(pdeck)

        # deal two cards to each player's hand
        playerhand = Hand()
        dealerhand = Hand()
        for n in 1,2:
            playerhand.add_card(pdeck.deal())
            dealerhand.add_card(pdeck.deal())

        # set up the Player's chips
        print(playerchips)

        if playerchips.total == 0:
            print("Sorry you run out of chips for this game.\n")
            break
        # prompt the Player for their bet
        take_bet(playerchips)

        # show cards but keep one dealer card hidden
        show_some(playerhand, dealerhand)

        while playing:
            # prompt for Player to Hit or Stand
            # class object can be changed through outside functions
            hit_or_stand(pdeck, playerhand)

            # # show cards (but keep one dealer card hidden)
            # show_some(playerhand, dealerhand)

            # if Player's hand exceeds 21, run player_busts() and break out of loop
            if playerhand.value > 21:
                player_busts(playerhand, playerchips)
                break

        # if Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if playerhand.value <= 21:
            # show all cards
            show_all(playerhand, dealerhand)
            while dealerhand.value < 17:
                hit(pdeck, dealerhand)
                print(f"Dealer value: {dealerhand.value}")
                time.sleep(3)
            print("\n"+20*"-")
            # run different winning scenarios
            if dealerhand.value > 21:
                dealer_busts(dealerhand, playerchips)
            else:
                if dealerhand.value > playerhand.value:
                    dealer_wins(dealerhand, playerhand, playerchips)
                elif dealerhand.value < playerhand.value:
                    player_wins(dealerhand, playerhand, playerchips)
                else:
                    push(dealerhand, playerhand)
            show_all(playerhand, dealerhand)

        # inform Player of their chips total
        print(playerchips)

        # ask to play again
        if not playagain():
            break
        else:
            playing = True
