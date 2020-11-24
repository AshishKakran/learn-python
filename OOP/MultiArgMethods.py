#!/usr/bin/python3

import math

class Point:
    def move(self,x,y):
        self.x=x
        self.y=y

    def reset(self):
        self.move(0,0)

    def calc_distance(self,ref_point):
        return math.sqrt(
                (self.x - ref_point.x)**2 +
                (self.y - ref_point.y)**2)

#how to use it:

p1 = Point()
p2 = Point()

p1.reset()
p2.move(5,0)

print(p2.calc_distance(p1))
assert (p2.calc_distance(p1) == p1.calc_distance(p2))

p1.move(3,4)

print(p1.calc_distance(p2))
print(p1.calc_distance(p1))
