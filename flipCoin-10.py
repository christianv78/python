#Flip a coin 10 times
#and print the results
import random

coin = ["heads", "tails"]
maxFlips = 10

def flipCoin():
	flip = 1
	totalHeads = 0
	totalTails = 0
	print() #space
	while flip <= maxFlips:
		outcome = random.randint(0,1)
		print(coin[outcome])
		if outcome == 0:
			totalHeads += 1
		elif outcome == 1:
			totalTails += 1
		flip += 1
	print() #space
	print("Heads total: ", totalHeads)
	print("Tails total: ", totalTails)
	print() #space

game = True
while game:
	answer = input(print("Flip a coin?  y/n"))
	if answer.lower().strip() == "y":
		flipCoin()
	else:
		print("goodbye")
		game = False