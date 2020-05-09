#!/usr/bin/python3

amount=12618.98
interestRate= 0.0013
interest = amount* interestRate
print("Interest is ", interest) #upto six decimal place it will be printed

#let's try formatting it to two decimal places

print("Interest is ", round(interest,2)) # print function loses out last 0 in rounded value

#Instead, let's try format function
#syntax format(item, format-specifier) returns string with specified format on item

print("Interest is", format(interest, ".2f")) #now it works

#more formatting

print(format(99.124562, "10.2f"))
print(format(12345679.123, "10.2f"))
print(format(57, "10.2f")) # format specifer width.precisionFloating-pointNum
#width guarantees minimum width required to format, if num is larger, actual printing characters exceed width

#scientific notation

print(format(12341.23235, "10.2e"))
print(format(12341.23235, "10.3e"))


#percentage format

print(format(34.22,".2%"))

#ofcourse we can justify format like we do in printf in C with flag

print(format(34.23535, "<10.2f")) #justify to left


#######################################
#formatting integers
# d=base10, x=base16, b=base2 , o=base8
#######################################


print(format(15, "10d"))
print(format(15, "10x"))
print(format(15, "10b"))
print(format(15, "10o"))

#strings can be formatted with format-specifier s

print(format("welcome to python", "20s"))
print(format("welcome to python 3", "<20s"))
print(format("welcome to python 3", "10.4s")) #notice what precision does to string, same behaviour as in C

