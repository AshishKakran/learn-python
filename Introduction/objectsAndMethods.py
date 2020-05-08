#!/usr/bin/python3

# in python everything is object

n=3 #n is an integer object 

print(id(n)) # id returns object's memory reference

print("type of ", n, " is ", type(n))

m=3.0
print("type of " ,m," is ", type(m))


s="Welcome"
print(s.lower()) #print in lowercase
print(s.upper()) #print in uppercase

s1="\t Welcome \n"
print(s1.strip()) #strip whitespace characters
