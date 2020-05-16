#!/usr/bin/python3
""" This helps you understand scope or namespace rules
    This example is taken from chapter 4 of 
    Introduction to Computation and Programming using Python
    by J guttag
"""
def f(x):
    def g():
        x="abc"
        print("x=",x)
    def h():
        z=x
        print("z=",z)
    x=x+1
    print("x=",x)
    h()
    g()
    print("x=",x)
    return g

def main():
    x=3
    z=f(x)
    print("x=",x)
    print("z=",z)
    z()

main()
