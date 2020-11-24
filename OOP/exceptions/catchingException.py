#!/usr/bin/env python3

def funny_div(integer):
    try: 
        if integer == 13: 
            raise ValueError("13 is evil")
        return 100/integer
    except (ZeroDivisionError, TypeError):
        return "wish you had studied math, can't divide by something silly as zero or string"

print(funny_div(50))
print(funny_div(0))
print(funny_div("haha"))
print(funny_div(13))
