#!/usr/bin/python3

import random

#generate random number

num1=random.randint(0,9)
num2=random.randint(0,9)

if num1 < num2 :
    num1,num2=num2,num1

answer= eval(input(f"what is {num1} - {num2}?")) # what if user enters nothing?

while num1 - num2 != answer:
    answer = eval(input("wrong answer. Try again?"))

print("you got it")
