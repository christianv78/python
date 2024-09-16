# "Toilet Seat"
# (hand-held solitaire game)
# to do:  Add stops and player choice so game
# does not auto-resolve

import random
from pprint import pprint

cards = [
	"A-hearts",
	"2-hearts",
	"3-hearts",
	"4-hearts",
	"5-hearts",
	"6-hearts",
	"7-hearts",
	"8-hearts",
	"9-hearts",
	"10-hearts",
	"J-hearts",
	"Q-hearts",
	"K-hearts",
	"A-diamonds",
	"2-diamonds",
	"3-diamonds",
	"4-diamonds",
	"5-diamonds",
	"6-diamonds",
	"7-diamonds",
	"8-diamonds",
	"9-diamonds",
	"10-diamonds",
	"J-diamonds",
	"Q-diamonds",
	"K-diamonds",
	"A-spades",
	"2-spades",
	"3-spades",
	"4-spades",
	"5-spades",
	"6-spades",
	"7-spades",
	"8-spades",
	"9-spades",
	"10-spades",
	"J-spades",
	"Q-spades",
	"K-spades",
	"A-clubs",
	"2-clubs",
	"3-clubs" ,
	"4-clubs",
	"5-clubs",
	"6-clubs",
	"7-clubs",
	"8-clubs",
	"9-clubs",
	"10-clubs",
	"J-clubs",
	"Q-clubs",
	"K-clubs"
]

"""RULES

1. Draw 4 cards.  If the two outer cards (1 and 4) have the same suit, discard inner two cards (2 and 3). Draw two more. Card 4 becomes card 2 (slides left).
2.  If the two outer cards have the same numerical value, discard all 4 and draw 4 new cards.
3.  If neither is true, draw another card. Last 4 cards are the ones in play.
3.  Goal is to end up with as few cards as possible in your hand."""


# make deck list from all cards
deck = []

for card in cards:
	deck.append(card)
	
	
hand = []	

# draw card function
def drawCard ():
	if len(deck) > 0:
		#numRemaining = len(deck)
		selection = random.choice(deck)
		deck.remove(selection)
		#suit = selection.split("-")[1]
		hand.append(selection)
		print("You drew: ", selection)
		return selection
		#return suit
	else:
		return

# make sure hand has at least 4 cards
def updateHand():		
	while len(hand) < 4:
		if len(deck) > 0:
			drawCard()
	remainingCards()


def showCurrentHand():
	numCards = len(hand)
	print()
	print("Current hand is", numCards, "cards: ")
	pprint(hand)
	print()


def compareCards():
	card1 = hand[-4]
	card2 = hand[-3]
	card3 = hand[-2]
	card4 = hand[-1]
	if card1.split("-")[1] == card4.split("-")[1]:
		print("First and last cards have the same suit!!!")
		# discard inner two cards
		print(card2, "and", card3, "removed from hand.")
		del hand[-3 : -1]
	elif card1.split("-")[0] == card4.split("-")[0]:
		print("First and last cards have the same value!!!")
		# discard last 4 cards
		print(card1, card2, card3, "and", card4, "removed from hand.")
		del hand[-4 : ]
	else:
		print("No match. Draw another card.")
		print()
		drawCard()

def remainingCards():
	print("There are", len(deck), "cards remaining.")



# MAIN GAME LOOP

while len(deck) > 0:
	updateHand()
	showCurrentHand()
	if len(hand) >= 4:
		compareCards()
	
	
if len(deck) == 0:
	#compareCards()
	print()
	print("Out of cards.")
	print()
	print("Final hand: ", hand)
	print()
	print("Your final score is: ", len(hand))
	
if len(deck) == 0 and len(hand) == 0:
	print("No cards left in your hand! Lucky you! Go buy a lottery ticket!")
	
	

	

	