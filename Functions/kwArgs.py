#!/usr/bin/python3

# you can use combo of postional, default and keyword arguments while invoking function

def parrot(voltage,state='a stiff', action='voom', type='Norwegian Blue'): #1 required arg, 3 optional args
    print("--This parrot wouldn't ", action, end=' ')
    print("if you put ", voltage, "volts throught it.")
    print("-- Lovely plumage, the ", type)
    print("-- It's ", state, "!")

def main():
    parrot(1000)                # 1 positional arg
    parrot(voltage=1000)        # 1 kw arg
    parrot(voltage=100000, action='vooooom') # 2 kw args
    parrot(action="vooom",voltage=1000) # kw args can appear in any order,but only after positional ones

main()

"""
Following calls would be invalid

parrot()
parrot(voltage=5, 'dead') # positional args can't follow keyword args
parrot(100,voltage=200)  #duplicate value for the same arg
parrot(actor="Keanu reeves") #unknown kw arg
"""
#checkout https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments 
