#!/usr/bin/python3

def f(x,y):
    """ Takes two argument and tries to modify them
        x is list type (Mutable object)
        y is int type (UnMutable object)
    """
    print("Id of parameters before modification:\n")
    print(f"id of list x is {id(x)}")
    print(f"id of int y is {id(y)}")
    x[1]=5
    y=10
    print("\nId of parameters after modification:\n")
    print(f"id of list x is {id(x)}")
    print(f"id of int y is {id(y)}")

def main():
    x=[1,2,3]
    y=4
    print("\nId in Main before call to f\n")
    print(f"id of list x is {id(x)}")
    print(f"id of int y is {id(y)}")

    print("x=",x[:])
    print("y=",y)

    print("\nIDs and values inside function:\n")
    f(x,y)

    print("\nId in Main after call to f")
    print(f"id of list x is {id(x)}")
    print(f"id of int y is {id(y)}")
    

    
    print("x=",x[:])
    print("y=",y)

main()
