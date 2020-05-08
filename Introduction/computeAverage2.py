#!/usr/bin/python3

#take three numbers as input

num1,num2,num3=eval(input("Enter three numbers separated by comma : "))
#what happens if you don't enter csv values? why does python complain about "int is not iterable"
#can we use other delimiter?

avg=(num1 +num2 +num3)/3 #notice how avg is floating point value

print("the average is " , avg)
