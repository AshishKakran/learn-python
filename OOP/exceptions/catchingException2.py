#!/usr/bin/env python3

def funny_div(integer):
    try: 
        if integer == 13: 
            raise ValueError("13 is evil")
        return 100/integer
    except ZeroDivisionError:
        print("can't divide by 0")
    except TypeError:
        print("Enter a numerical value")
    except ValueError:
        print("well 13 is evil, avoid it")
        #raise raise #this syntax is probably depreciated

print(funny_div(50))
print(funny_div(0))
print(funny_div("haha"))
print(funny_div(13))
