#!/usr/bin/python3

class Point:
    def reset(self):
        self.x=0
        self.y=0

p=Point()
p.reset()   #call the method on the object

print(p.x,p.y)

q=Point()


Point.reset(q)  #call the method on the class and explicitly pass object

print(q.x,q.y)
