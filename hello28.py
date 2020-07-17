#This is a birthday match game.
import random
print ('Hello! My name is Alice.')
print ('What is your name?')
myName = input()

realDay = random.randint(1, 30)
print ('Well, ' + myName + ', guess my birthday from 1 to 30.')

trial = 0
while trial < 5 :
    trial = trial + 1
    guessDay = int(input())

    if guessDay < realDay :
        print ('Guess a later day.')
    if guessDay > realDay :
        print ('Guess an earlier day.')
    if guessDay == realDay :
        print ('Good job! ' + myName + '.')
