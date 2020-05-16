#!/usr/bin/python3

def fib(n):
    a,b=0,1

    while a < n:
        print(a)
        a,b=b,a+b


def main():
    h=fib #assign ref to function to h
    h(100) #execute instruction kept at ref hold by h

main()
