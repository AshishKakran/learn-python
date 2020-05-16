#!/usr/bin/python3

def ask_ok(prompt,retries=4,reminder='Please try again!'): 
    while True:
        ok = input(prompt)
        if ok in ('y',  'ye', 'yes'):
            return True
        if ok in ('n','no', 'nop','nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def main():
    prompt="Do you really wanna quit?"
    if ask_ok(prompt,5): #notice we haven't supplied reference for reminders, default value takes care of this
        print("cool")
    else:
        print("you are boring")

main()
    
    
#note: default values are evaluated only once, so if you pass mutable objects as default values, changing those objects will change default value b/w subsequent calls
"""
def f(x,l=[1]):
    l[0]=x
    return l
try calling this function multiple times with different values of x
"""

