#!/usr/bin/python3
import random

#generate random numbers

num1=random.randint(0,9)
num2=random.randint(0,9)

#prompt

answer=eval(input(f"what is {num1} + {num2} equals?"))

# relational operators
print("{} + {} = {} is {}".format(num1,num2,answer, num1+num2 == answer))
