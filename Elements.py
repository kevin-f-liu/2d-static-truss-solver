import math
import numpy as np

class Node:
    def __init__(self, name, loc):
        self.id = name
        self.x = loc[0]
        self.y = loc[1]
        # List of Trusses that connect
        self.connections = []
        # External Forces on the Node
        self.external = []
        # Constant cost
        self.cost = 6

class Force:
    # External forces
    def __init__(self, node, vector):
        self.id = node
        self.val = vector[0]
        # Angle out of 360
        self.direction = vector[1]

class Truss:
    def __init__(self, t):
        # Strings
        self.startID = t[0]
        self.endID = t[1]

        self.startx = None
        self.starty = None
        self.endx = None
        self.endy = None
        # Visit. On first usage in matrix it is positive, on second it is false
        self.xlength = None
        self.ylength = None
        self.length = None
        self.cost = None

    def calcLengths(self):
        self.xlength = self.startx - self.endx
        self.ylength = self.starty - self.endy
        self.length = math.sqrt(self.xlength ** 2 + self.ylength ** 2)
        self.cost = self.length * 12

    def setStart(self, loc):
        self.startx = loc[0]
        self.starty = loc[1]
        if self.endx is not None:
            self.calcLengths()

    def setEnd(self, loc):
        self.endx = loc[0]
        self.endy = loc[1]
        if self.startx is not None:
            self.calcLengths()
