#!/usr/bin/env python3

def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never exectue")
    return "I won't be returned"

def call_exceptor():
    print("call_exceptor starts here")
    no_return()
    print("an exeption was raised..")
    print("...so these lines don't run")


call_exceptor() 
'''exception however don't immediately terminates execution, it can be handled at any level
interpreter exits only when exception is not handled at any the level, here after 
no_return encounters an exception and interpreter looks whether call_exceptor can handle it
since it cannot, it raises the same error and execution stops.''' 
