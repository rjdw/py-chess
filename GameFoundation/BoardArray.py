import ../Pieces.*
import Location

#Created by richardwang007 on 8/02/17
class BoardArray(object):

    # makes the board of row and col length
    def __init__(self, rows, cols):
        self.board = [x[:] for x in [[None]*cols]*rows]



    # returns the number of rows
    def getNumRows(self):
        return len(self.board)


    # returns the number of cols
    def getNumCols(self):
        return len(self.board[0])

    # Determines if a location on the board is valid
    # True if isValid else false
    def isValid(self, loc):
        return (loc.getRow()>=0 and loc.getRow()<self.getNumRows()
                and loc.getCol()>=0 and loc.getCol()<self.getNumCols())


    #returns the object at the given location on the board
    #if the location is not valid, it raises an error
    #if the location is empty it returns None
    def get(self, loc):
        if (not self.isValid(loc)):
            raise ValueError("Location " + loc
                    + " is not valid")
        return board[loc.getRow()][loc.getCol()]

    #Puts an object in a selected location on the grid
    #returns the object previously occupying the location
    #or None if the location was empty
    def put(self, loc, obj):
        if (!self.isValid(loc)):
            raise ValueError("Location " + loc
                    + " is not valid")
        if (obj == None):
            raise ValueError("Object is None")
        removed = self.get(loc)
        board[loc.getRow()][loc.getCol()] = obj
        return removed

    #removes the element at the location on the grid
    #then returns that element
    #returns None if that location is empty
    def remove(self, loc):
        if (not self.isValid(loc)):
            raise ValueError("Location " + loc
                    + " is not valid")
        removed = self.get(loc)
        board[loc.getRow()][loc.getCol()] = None
        return removed


    #returns all the occupied locations on the grid
    def getOccupiedLocations(self):
        locations = []
        for i in range(self.getNumRows()):
            for k in range(self.getNumCols()):
                loc = Location(i, k)
                if (self.get(loc) != None):
                    locations.append(loc)
        return locations

    # returns all Pawn instances on the board
    def getPawns(self):
        locations = self.getOccupiedLocations()
        result = []
        for loc in locations:
            pos = self.get(loc)
            if (type(pos) is Pawn):
                result.append(pos)
        return result


    # returns all Knight instances n board
    def getKnights(self):
        locations = self.getOccupiedLocations()
        result =[]
        for loc in locations:
            pos = self.get(loc)
            if (type(pos) is Knight):
                result.append(pos)
        return result

    #returns all Rook instances on board
    def getRooks(self):
        locations = self.getOccupiedLocations()
        result = []
        for loc in locations:
            pos = self.get(loc)
            if (type(pos) is Rook):
                result.append(pos)
        return result
