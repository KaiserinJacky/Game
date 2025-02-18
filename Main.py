# old solitaire game code - probably don't need but i'd like to have it as a reference for now

import random # needed to shuffle deck

class Card: # define card class
    def __init__(self, kind, value):
        self.kind = kind # monster, potion, or weapon
        self.value = value

    def __str__(self): # string to print
        if self.kind == "Null":
            return f"Empty"
        return f"{self.kind}, {self.value}"

class Weapon: # define weapon class
    def __init__(self, card):
        self.value = card.value # the card's value
        self.strength = 15 # starting strength of every weapon

    def __str__(self):  # string to print
        if self.value == 0:
            return f"No Weapon"
        return f"{self.value}, {self.strength}"

def deal(deck, room): # deal cards to room
    for i in range(4):
        if room[i] == nullc:
            if len(deck) > 0:
                room[i] = deck.pop(0)

def display():
    y = 1
    for i in room:
        print(y, ":", i)
        y += 1
    print("HP:", HP, "/ 20")
    print("Remaining Cards in Deck:", len(deck))
    print("Weapon:", wep)

# initialize
HP = 20 # starting health
game = True # bool that controls game
nullc = Card("Null",0) # define null card
deck = [nullc] * 44 # fill deck with null cards
room = [nullc] * 4 # fill room with null cards
wep = Weapon(nullc) # set first weapon to null card
inp = 0 # initialize input
canrun = True # can run on first room

# fill deck
for i in range(13): # monsters
  #spades
  deck[i] = Card("Monster", i+2)
  #clubs
  deck[13 + i] = Card("Monster", i+2)
for i in range(9): # add potions
    deck[26 + i] = Card("Potion",i + 2)
for i in range(9): #add weapons
    deck[35 + i] = Card("Weapon", i + 2)

random.shuffle(deck) # shuffle the deck
deal(deck, room) # deal cards to the room
while game:
    display() # show board
    inp = input() # get input
    if inp == "run": # run
        if canrun:
            print("Running Away!")
            canrun = False
            for i in range(4):
                deck.append(room[i])
                room[i] = nullc
                deal(deck,room)
        else:
            print("Can't Run!")
    else: # chose a card
        try:
            move = int(inp) - 1 # get input
        except:
            move = "xnopyt"
        if move not in range(4):
            move = "xnopyt"
            print("Invalid Move! Try Again")
        elif room[move].kind == "Monster":
            #if value is less than str and weapon isn't nullc, prompt for weapon
            if room[move].value < wep.strength and wep.value != 0:
                attack = int(input("Use Weapon (1) or Barehanded (2)? "))
                if attack == 1:
                    if room[move].value > wep.value: # block damage
                        HP -= room[move].value - wep.value
                    wep.strength = room[move].value # reduce strength
                else:
                    HP -= room[move].value
            else:
                HP -= room[move].value
            print("Fought a Monster!")
        elif room[move].kind == "Potion":
            HP += room[move].value # heal by value up to max
            if HP > 20:
                HP = 20
            print("Healed by", room[move].value)
        elif room[move].kind == "Weapon":
            wep = Weapon(room[move])
            print("Obtained New Weapon!")
        elif room[move].kind == "Null":
            print("Empty! Choose Another Card")
        if move != "xnopyt":
           room[move] = nullc # set card to empty

    if HP < 1: # lose condition
        print("You Died!")
        game = False

    if game: #keeps anything from happening if you lose
        counter = 0
        for i in room: # check for win
            if i == nullc:
                counter += 1
            if counter == 4 and len(deck) == 0: # win condition
                print("Congratulations! You beat the game!")
                game = False
    if game: #keeps anything from happening if you win
        counter = 0 # reset counter
        for i in room: # check for room reset
            if i == nullc:
                counter += 1
            if counter == 3:
                print("Entering new room...")
                canrun = True
                deal(deck, room)
                counter = 1