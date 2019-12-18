import math
# Created by richardwang007 on 8/02/17
class Location(object):
    #DO NOT MODIFY!!!!!
    #PUBLIC STATIC FINAL!!!! :P
    __directions = {
    "left" : -90,
    "right" : 90,
    "half_left" : -45,
    "half_right" : 45,
    "full_circle" : 360,
    "half_circle" : 180,
    "north" : 0,
    "northeast" : 45,
    "east" : 90,
    "southeast" : 135,
    "south" : 180,
    "southwest" : 225,
    "west" : 270,
    "northwest" : 315}

    #contructor for location
    #takes in a row and a col
    def __init__(self, int r, int c):
        self.row = r
        self.col = c

    #gets the row of a location object
    def getRow(self):
        return self.row

    #gets the col of a location object
    def getCol(self):
        return col

    #creates location string
    def __str__(self):
        return "(" + self.getRow() + ", " + self.getCol() + ")"

    #for equal operator
    def __eq__(self, other):
        if (not isinstance(other, Location)):
            return False
        return self.getRow()==other.getRow() and self.getCol()==other.getCol()

    #returns a location object adjacent to this
    #in the direction specified
    def getAdjacentLocation(self, direction):
        #rouds to mulitples of 45
        #because those represent directions and half directions correctly
        adjustedDirection = (direction + self.__directions["half_right"] / 2) %
                            self.__directions['full_circle']
        if (adjustedDirection < 0):
            adjustedDirection += self.__directions['full_circle']
        adjustedDirection = (adjustedDirection // self.__directions['half_right']) *
                            self.__directions['half_right']
        dc, dr = 0, 0
        if self.__directions['east'] == adjustedDirection:
            dc=1
        elif self.__directions['southeast'] == adjustedDirection:
            dc=1
            dr=1
        elif self.__directions['south'] == adjustedDirection:
            dr=1
        elif self.__directions['southwest'] == adjustedDirection:
            dc=-1
            dr=1
        elif self.__directions['west'] == adjustedDirection:
            dc=-1
        elif self.__directions['northwest'] == adjustedDirection:
            dc=-1
            dr=-1
        elif self.__directions['north'] == adjustedDirection:
            dr=-1
        elif self.__directions['northeast'] == adjustedDirection:
            dc = 1
            dr =-1
        return Location(self.getRow() + dr, self.getCol() + dc)

    # Returns the direction from this location toward another location
    # rounded to the nearest compass direction
    def getDirectionToward(self, target):
        dx = target.getCol() - self.getCol()
        dy = target.getRow() - self.getRow()
        angle = math.degrees(math.atan2(-dy, dx))
        #currently counterclockwise
        #make clockwise
        compassAngle = self.__directions['right'] - angle
        compassAngle += self.__directions['half_right']//2
        #negative case
        if (compassAngle < 0)
            compassAngle += self.__directions['full_circle']
        #round
        return (compassAngle // self.__directions['half_right']) *
                self.__directions['half_right']

    # compares two locations
    # returns -1 if self is less than other
    # 1 is self is greater than other
    # 0 if equal
    #like in java comparable LOL
    def compareTo(self, other):
        if(not isinstance(other, Location)):
            raise ValueError(other "not location")
        if (self.getRow() < other.getRow()):
            return -1
        if (self.getRow() > otherLoc.getRow()):
            return 1
        if (self.getCol() < otherLoc.getCol()):
            return -1
        if (self.getCol() > otherLoc.getCol()):
            return 1
        return 0
