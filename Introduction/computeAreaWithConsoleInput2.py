#!/usr/bin/python3
#above line tells shell to invoke python3 interpreter to run this script

#calculate area of circle

#prompt  the user to enter a radius
prompt="Enter a radius" #poor prompt

radius=eval(input(prompt)) #cleaner code/could be confusing in larger program 

#self note : understand how input, print and eval function works

#compute area
area=radius * radius * 3.14159 #python is dynamically typed, so we don't need to declare type of variables

#display results using print
print("The are of circle of radius", radius, "is", area)
