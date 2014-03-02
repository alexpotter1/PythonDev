# blackjack game

import random

score = 0 # player's score
card = 0 # this is a value between 1 and 10
CPUscore = 0

name = input("What's your name? ")

def getCard():
    return random.randrange(1,10)

def drawCard(player):
    card = getCard()
    print("%s drew %i" % (player,card))
    return card



score += drawCard(name)
score += drawCard(name)

CPUscore += drawCard("CPU")
CPUscore += drawCard("CPU")
    
print("%s has %i" % (name,score))
print("CPU has %i" % CPUscore)

while score <= 21:

    response = str(input("Draw another card? [Y/n] "))

    if response == 'Y' or response == 'y':
        score+= drawCard(name)
        print("Your score is %i" % score)
    else:
        print("Your score is %i" % score)
        break

    while CPUscore <= 17:
        CPUscore += drawCard("CPU")
        print("CPU has %i" % CPUscore)
    
if score > 21:
    print("You lose")
elif score <= 21 and CPUscore > 21:
    print("CPU loses")
elif score == 21 and CPUscore == 21:
    print("You lose (House rules)")
elif score < CPUscore and CPUscore <= 21:
    print("You lose")
else:
    print("You win")
    
    
    
