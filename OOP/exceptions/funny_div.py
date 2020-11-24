#!/usr/bin/env python3

def funny_div(num):
    try:

        if num == 13:
            raise ValueError("13 is evil")
        return 100/num
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No,no not 13")
