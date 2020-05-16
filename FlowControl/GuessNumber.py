#!/usr/bin/python3

import random

num=random.randint(0,100)

print("Computer generated a number b/w 0 and 100..Guess that")

guess=-1 # initialization of loop

while guess != num:
    guess=eval(input())
    proximity=abs(guess-num)
    if proximity < 5:
        print("You are very close,try again")
    elif proximity < 10: 
        print("A little closer, try again")
    else:
        print("poor guess, try again")

print("You got it")
