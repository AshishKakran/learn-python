#!/usr/bin/python3

def fib(n):
    """Print a Fibonacci series up to n"""
    a,b=0,1
    while a < n:
        print(a,end=' ')
        a,b=b,a+b
    print()

def main():
    fib(2000) # a void function aka None Function 


main()

