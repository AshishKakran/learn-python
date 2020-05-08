#!/usr/bin/python3

#take three numbers as input

num1=eval(input("enter first number: "))
num2=eval(input("enter 2nd number: "))
num3=eval(input("enter 3rd number: "))

#alternatively we can use num1,num2,num3=eval(input(prompt))
#of course that involves dependency from user to enter csv values

avg=(num1 +num2 +num3)/3

print("The average of ", num1,num2,num3, "is", avg)
