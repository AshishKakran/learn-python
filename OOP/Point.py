#!/usr/bin/python3

import math

class Point:
    'Represents a point in the two-dimensional geometric coordinates system'

    def __init__(self,x=0,y=0):
        '''Initialize the position of a new point.
            The x and y coordinates are optional'''
        self.move(x,y)

    def move(self,x,y):
        "Move the point to a new location in 2-d space"
        self.x=x
        self.y=y

    def reset(self):
        'Reset the point back to the origin 0,0'
        self.move(0,0)

    def calc_dist(self,ref_point):
        """ Calculate the distance between point to a ref_point"""
        return math.sqrt( (self.x - ref_point.x)**2 + (self.y - ref_point.y)**2)


