#!/usr/bin/python3

def cheeseShop(kind,*arguments, **keywords):
    print("--Do you have any " + kind + "?")
    print("--I'm sorry. we're all out of " + kind)
    for arg in arguments:
        print(arg)
    print("-"*40)

    for kw in keywords:
        print(kw,":",keywords[kw])


cheeseShop("Hulk A Hulk burning fudge", "It's runny", "It's very runny", shopkeeper="Ashish",client="Hulk", sketch="CheeseShop")


"""
When a final formal parameter of the form **name is present, it receives a dictionary 
containing all keyword arguments except for those corresponding to a formal parameter.
This may be combined with a formal parameter of the form *name ,
which receives a tuple containing the positional arguments beyond the formal parameter list. 
(*name must occur before **name.)
"""
