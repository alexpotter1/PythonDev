import random


gameInProgress = 1
num = random.randrange(1,10)



while gameInProgress == 1:
    answer = int(input('Guess a number: '))
    if(answer == num):
        print('You win! The answer was: %d' % num)
        gameInProgress = 0
    else:
        if(answer > num):
            print('The number is lower!')
        elif(answer < num):
            print('The number is higher!')
        



