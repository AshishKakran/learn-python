#!/usr/bin/python3

class Point:
    def __init__(self,x=0,y=0):
        self.move(x,y)

    def move(self,x,y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

#construct a point
p = Point(1,2)

print(p.x,p.y)

z = Point()

print(z.x,z.y)
