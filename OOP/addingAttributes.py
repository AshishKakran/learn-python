#!/usr/bin/python3

class Point:    #create a dummy class
    pass

p1 = Point()    #create objects
p2 = Point()

p1.x = 5        #add attributes to instantiated objects 
p1.y = 4        #we don't modify class definition to add attributes 

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)
