'''5 Fruit Machine
Write a program to simulate a Fruit Machine that displays three symbols at random from 
Cherry, Bell, Lemon, Orange, Star, Skull.
The player starts with £1 credit, with each go costing 20p. 
If the Fruit Machine “rolls” two of the same symbol, 
the user wins 50p. The player wins £1 for three of the same and £5 for 3
Bells. The player loses £1 if two skulls are rolled and all of his/her money if three skulls are rolled. The player can choose to quit with the winnings after each roll or keep playing until
there is no money left.'''

import random

symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]
credit = 100

while credit >= 20:
    print("your credit is £",(credit/100))
    input("press enter to play (20p charge)")
    credit -= 20

    #choose the fruit
    fruitChoice = (symbols[random.randint(0,5)],symbols[random.randint(0,5)],symbols[random.randint(0,5)])
    print(fruitChoice)

    #2 the same
    if len(set(fruitChoice)) == 2:
        if fruitChoice.count("Skull")==2:
            creditChange = -100
        else:
            creditChange = 50

    #3 the same
    elif len(set(fruitChoice)) == 1:
        if "Bell" in fruitChoice:
            creditChange = 500
        else:
            creditChange = 100
    else:
             creditChange = 0

    #work out new credit
    credit += creditChange
    print ("You won £", creditChange/100)

print ("You're out of credit, sorry.")

