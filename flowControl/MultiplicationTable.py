#!/usr/bin/python3

print("\t\tMultiplication Table")

#Display Multiplicand 

print("   ", end=" ")

for i in range(1,10):
    print("{:6d}".format(i), end=" ")

print("\n-------------------------------------------------------------------")

#Display Multipliers and Values

for i in range(1,10):
    print(f"{i} |", end=" ")
    for j in range(1,10):
        print("{:6d}".format(i*j),end=" ")
    print()

