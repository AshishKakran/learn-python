#!/usr/bin/python3

#There are two ways to format a string
# f"string" style
# string.format() style

# f"string"

x=10
y=20
print(f" {x} + {y} equals {x+y}")  # {} this is called a replacement field

#string.format() style

formatter=" {} {} equals {} "

print(formatter.format(x,y,x+y))

formatter=" {1} {0} equals {2} "

print(formatter.format(x,y,x+y)) # see pydoc FORMATTING for full grammar of {replacement fields}


