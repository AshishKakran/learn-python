#!/usr/bin/python3
from sys import exit
# Take height from the user

try:
    height=eval(input("To generate pyramid, enter a height"))
except (EOFError):
    print("\nYou are boring\n")
    exit(1)

if height > 12 or height < 0 :
    print("Respect computers bro")
    exit(100)

for m in range(0,height):
    #print spaces first, height - m spaces
    print(" "* 5* (height -m), end="")

    #print first half --> 2**0 through 2**m
    for power in range(0, m+1):
        print("{:5d}".format(2**power), end="")

    #print 2nd half --> 2**m-1 through 2**0
    for power in range(m-1,-1,-1):
        print("{:5d}".format(2**power), end="")
    print()
    
    
