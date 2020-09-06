# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:30:10 2020

@author: lohit
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:56:20 2020

@author: lohit
"""
import random
suits = ('Hearts','Diamonds','Spade','Club')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = { 'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

# card attributes: suit, rank
# methods : print

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+" of "+self.suit

# Deck attributes Deck
# methods: shuffle, __str__, deal

class Deck():

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return 'the deck has:'+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return (self.deck.pop())

# Hand, attributes: cards in hand,sum of value of cards, number of aces
# methods : add card to hand, adjust for ace

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces += 1

# chips, attributes: total and subreport
# methods: win bet, lose bet

class Chips():

    def __init__(self):
        self.total =100
        self.bet= 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# fun for take bet, chip obj is passed as param

def take_bet(chips):
    # ask user input until it receives int and < than total
    while True:
        try:
            chips.bet = int(input("choose you bet amount:"))
        except:
            print('oops, thats not an integer,, try again')
        else:
            if chips.bet > chips.total:
                print('oops, bet cant be more than', chips.total)
            else:
                break

# fun hit, hand and deck objs are passed to pull card from deck_comp..

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# func to take input, hit or stay

def hit_or_stand(deck,hand):

    global playing

    while True:
        x = input('would you like to hit or stay, h or s:')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('player choose to stay, dealer is playing')
            playing = False
        else:
            # cotinue to ask input
            continue
        break
# show one head up and one head down while player is still playing

def show_some(player, dealer):
    print('\n\nDealers hand:')
    print('<card hidden>')
    print(dealer.cards[1])
    print('\n\nPlayers hand:',*player.cards,sep='\n')
    print('Players value:',player.value)

# show all cards in dealer hand

def show_all(player,dealer):
    print('\n\nDealers hand:', *dealer.cards, sep='\n')
    print('Dealers value:',dealer.value)
    print('\n\nPlayers hand:',*player.cards,sep='\n')
    print('Players value:',player.value)

# funcs for dealer burts, wins and player burts, wins and push( tie)

def dealer_busts(player,dealer,chips):
    print('dealer busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('dealer wins!')
    chips.lose_bet()

def player_busts(player,dealer, chips):
    print('player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('player wins!')
    chips.win_bet()

def push(player,dealer):
    print('player and dealer are tie!')

while True:

    print('welcome to blackjack, choose close to 21 as you can, without crossing\n\
    dealer hits until it cross player or busts, aces count as 1 or 11')

    # create deck and shuffle

    deck = Deck()
    deck.shuffle()

    # create player and dealer hand and pull 2-2 cards

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # create chips and take bet from user

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    # while player is playing ask hit or stay and display 1 card of dealer_hand

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

        # hit until dealer_hand crosses player or dealer_busts
        print('\n\ncards before dealer starts playing:')
        show_all(player_hand,dealer_hand)

        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
            show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('Players winnings are at stand ',player_chips.total)

    new_game = input('want to play another hand y or n:')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('thanks for playing')
        break
