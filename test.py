import random
from random import shuffle

def RANKS(): return ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
def SUITS(): return ['h','d','s','c']

class Savefile:
    def __init__( self, keptCards, fh ):
         fh.write("\n" + keptCards + ",")
        
    
    


class Card:
    def __init__( self, rank, suit ):
        self.rank = rank
        self.suit = suit
    
    def __str__( self ):
        return self.rank + self.suit
        
class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [Card( rank, suit) for rank in RANKS() for suit in SUITS()]
        for x in range(5):
            random.shuffle( self.contents )
        

class Main:

    fh = open('demo.csv', 'a')
    x = input("press n for new hand or q to quit: \n")
    while x != 'q':

        deck = Deck()

        hand = str(deck.contents[0]) + "-" + str(deck.contents[1])
        if hand[1] == hand[4]:
            hand = hand[0]+hand[3]+"S"
        else:
            hand = hand[0]+hand[3]+"oS"
        print(hand)

        choice = input( "f to fold, k to keep:\n")

        if choice == "f":
            print ( "you have folded." )
        elif choice == "k":
            print ( "you have kept your hand.")
            Savefile(hand,fh)
        else:
            print ( "invlaid input.")  
        
        x = input("press n for new hand or q to quit: \n")

    fh.close()
    exit()