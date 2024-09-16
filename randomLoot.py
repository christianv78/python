import random
from pprint import pprint
from time import sleep

# colored terminal text
# https://pypi.org/project/termcolor/
from termcolor import colored, cprint

# progress bar
from tqdm import tqdm

totalValue = 0

# Luck increases chance of better item rarity
# default is 0
luck = 0 # +5/10/15/20/25 

#speed default is 1
speed = 1 # +.5/.75/1.0/1.25/1.5

openChestTime = (3.5 - speed)  # default time to open chest is 2.5 seconds

receivedItems = []

items = {
    "guns" : [
        "Pistol",
        "Silenced Pistol",
        "Revolver",
        "SMG",
        "Pump Shotgun",
        "Double Barrel Shotgun",
        "Tactical Shotgun",
        "Hunting Rifle",
        "Assault Rifle",
        "Sniper Rifle",
        "Light Machine Gun",
        "Gattling Gun",
        "RPG",
        "Guided Rockets",
        "Rail Gun"
    ],
    "items" : [
        "Frag Grenades",
        "Cluster Grenades",
        "Molotov Cocktails",
        "Claymore Mines",
        "Smoke Grenade",
        "Door Alarm Trap",
        "Gold",
        "Ammo: Pistol",
        "Ammo: Rifle",
        "Ammo: Shotgun",
        "Ammo: Rockets",
        "Ammo: Energy"
    ], 
    "health" : [
        "Small Medkit",
        "Large Medkit",
        "Adrenaline Shot",
        "Pain Pills"
    ],
    "cards" : [
        "Luck Boost",
        "Speed Boost",
        "XP Boost",
        "Heightened Awareness",
        "Quiet Movement" 
        # card rarity +5/10/15/20/25% 
    ]  
}


# GET RANDOM RARITY BY % CHANCE

commonChance = 45 # 45%
uncommonChance = 75 # 30%
rareChance = 90 # 15%
epicChance = 99 # 9%
legendaryChance = 100 # 1%

rarity = "none"

def getRandomRarity():
    number = random.randint(1,100) + luck
    #print("Rarity number: ", number)
    if number <= commonChance:
        print("Common")
        return "common"
    elif number > commonChance and number <= uncommonChance:
        cprint("Uncommon", "green")
        return "uncommon"
    elif number > uncommonChance and number <= rareChance:
        cprint("Rare", "blue")
        return "rare"
    elif number > rareChance and number <= epicChance:
        cprint ("Epic", "magenta")
        return "epic"
    else:
        cprint("Legendary", "yellow")
        return "legendary"
	

# GET RANDOM CATEGORY TYPE BY %
gunChance = 36
itemChance = 32
healthChance = 30
cardChance = 2

category = "none"

def getRandomType():
    #global category
    number = random.randint(1,101)
    #print(number)
    if number <= gunChance:
        getRandomRarity()
        #print("gun")
        #category = "guns"
        return "guns"
    elif number > gunChance and number <= gunChance + itemChance:
        #print("item")
        #category = "items"
        return "items"
    elif number > gunChance + itemChance and number <= gunChance + itemChance + healthChance:
        #print("health")
        #category = "health"
        return "health"
    else:
        #print("card")
        getRandomRarity()
        #category = "cards" 
        return "cards"


#GET RANDOM ITEM OF GIVEN TYPE

randItem = "none"

def getRandomItem(category):
    #global randItem
    length = len(items.get(category))
    randItem = items.get(category)[random.randint(0, length - 1)]
    #receivedItems.append(randItem)  # add to list
    # Remove received item from list so you can't get 2
    # of the same thing in one chest
    items.get(category).remove(randItem)
    return randItem


# OPEN CHEST AND GET X ITEMS

def openChest(amount):
    count = 0
    print("Opening Chest...")
    for i in tqdm(range(100), desc = "opening..."):
        # The following sleep time should be affected by speed stat
        sleep(.01 * openChestTime)
    print()
    print("You got", amount, "items!")
    print()
    sleep(.5)
    for x in range(0, amount):
        sleep(.25)
        count += 1
        print(str(count) + ":")
        category = getRandomType()
        print("(" + category + ")")
        randItem = getRandomItem(category)
        print(randItem)
        print()
      
  
###########################
def choose():
	
	choice = input("Open a chest? (y/n) :").lower().strip()
	
	if choice == "y":
		openChest(random.randint(3,5))
		choose()
	elif choice == "n":
		print("Goodbye!")
		quit
	else:
		print("Invalid choice. Try again.")
		choose()

choose()

###########################

# SPEED DEBUG
#print("(Speed is", str(speed) + ". Time to open chest: ", str(openChestTime), "seconds.)")





