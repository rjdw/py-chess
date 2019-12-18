from tkinter import *
#created by richard wang on 8/05
#got ideas for structure and implementation from
#pieces I wrote in java previously
#chess images taken from http://i.imgur.com/zwF4Lyn.png
class Piece(object):
    #constructor for piece
    def __init__(self, pieceName, note, loc, brd, col, val, plCol):
        #instance variables
        self.imageFileName = pieceName
        self.possibleMovesArray=[]
        self.attackedPiecesArray = []
        self.board = brd
        self.location = loc
        self.color = col
        self.value = val
        self.notation = note
        self.playerCol = plCol
        self.pieceName = pieceName

        if self.color == "white":
            self.imageFileName = "W" + self.imageFileName
        else:
            self.imageFileName = "B" + self.imageFileName

    #returns a copy
    def copy(self):
        return Piece(self.pieceName, self.notation, self.location, self.board,
                    self.color, self.value, self.playerCol)

    #gets board
    def getBoard(self): return self.board

    #gets location
    def getLocation(self): return self.location

    #gets image file name
    def getImageFileName(self): return self.imageFileName

    #sets image file name
    def setImageFileName(self, name): self.imageFileName = name

    #gets the attackedPiecesArray
    def getAttackedPiecesArray(self):
        return self.attackedPiecesArray

    #sets possibleMovesArray
    def setPossibleMovesArray(self, pos):
        self.possibleMovesArray = pos

    #sets attackedPiecesArray
    def setAttackedPiecesArray(self, attacked):
        self.attackedPiecesArray = attacked

    #gets possibleMovesArray
    def getPossibleMovesArray(self):
        return self.possibleMovesArray

    # gets color
    def getColor(self): return self.color

    #sets color
    def setColor(self, col): self.color = col

    #gets value
    def getValue(self): return self.value

    #sets value
    def setValue(self, val): self.value = val

    #sets notation
    def setNotation(self, note): self.notation = note

    #gets notation
    def getNotation(self): return self.notation

    #sets the location
    def setLocation(self, loc): self.location = loc

    #sets the playerCol
    def setPlayerCol(self, playerCol1): self.playerCol = playerCol1

    #gets the playerCol
    def getPlayerCol(self): return self.playerCol

    #to string
    def __str__(self):
        #will add more later maybe
        loc = self.getLocation()
        row, col = loc.getRow(), loc.getCol()
        return self.pieceName + str((row, col))

    def __eq__(self, other):
        return type(self) == type(other)

    #removes self from its board
    def removeSelfFromGrid(self):
        if (self.board == None):
            raise Exception('piece not in a board')
        if (self.board.get(self.location) != self):
            raise Exception('piece no in' + str(self.location))
        self.board.remove(self.location)
        self.board = None
        self.location = None

    #puts itself into the board at loc
    #removes current object at loc
    def putSelfInGrid(self, gr, loc):
        piece = gr.get(loc)
        if (piece != None):
            piece.removeSelfFromGrid()
        gr.put(loc, self)
        self.board = gr
        self.location = loc

    #moves piece to the newLocation
    #removes and returns object currently in newLocation
    def moveTo(self, newLocation):
        if (self.board == None):
            raise Exception('not currently in grid')
        if (not self.board.isValid(newLocation)):
            raise ValueError(str(newLocation) + 'not valid')
        if (newLocation == self.location):
            return None
        self.board.remove(self.location)
        occupant = self.board.get(newLocation)
        if (occupant != None):
            occupant.removeSelfFromGrid()
        self.location = newLocation
        self.board.put(self.location, self)
        return occupant

    # Attempts to move the piece
    # returns null if the move is successful and the isn't a capture
    #          the captured piece if there is one
    #          False if the move is unsuccessful

    #MAYBE COMPLETELY WRONG
    def move(self, loc):
        board = self.getBoard()
        col = self.getColor()
        playerCol = self.getPlayerCol()
        location = self.getLocation()
        attackedPiecesArray = self.getAttackedPiecesArray()
        possibleMovesArray = self.getPossibleMovesArray()
        #check validity of loc
        if (loc in possibleMovesArray):
            return self.moveTo(loc)
        return False


#created by richard wang 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Queen(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("QUEEN", "Q", loc, brd, col, 9, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets attackedPiecesArray
    #call before setPossibleMovesArray
    def setAttackedPiecesArray(self):
        board = self.getBoard()
        pos = self._getIntersectingLocations()
        result = []
        for loc in pos:
            posAttacked = board.get(loc)
            if (posAttacked!=None):
                result.append(posAttacked)
        super().setAttackedPiecesArray(result)

    #sets the possibleMovesArray
    def setPossibleMovesArray(self):
        result = self._getIntersectingLocations()
        super().setPossibleMovesArray(result)

    #gets locations intersecting the current location
    def _getIntersectingLocations(self):
        result = []
        loc = self.getLocation()
        color = self.getColor()
        board = self.getBoard()
        currow = loc.getRow()
        curcol = loc.getCol()
        #top left
        currow-=1
        curcol-=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow-=1
            curcol-=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom right
        currow+=1
        curcol+=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow+=1
            curcol+=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #top right
        currow-=1
        curcol+=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor()==color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow-=1
            curcol+=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom left
        currow+=1
        curcol-=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow+=1
            curcol-=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #straight down
        currow+=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(Location(currow, curcol)).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow+=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        #straight up
        currow-=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(Location(currow, curcol)).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            currow-=1
            testLoc = Location(currow, curcol)
        currow = loc.getRow()
        #straight left
        curcol-=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            curcol-=1
            testLoc = Location(currow, curcol)
        curcol = loc.getCol()
        #straight right
        curcol+=1
        testLoc = Location(currow, curcol)
        while (board.isValid(testLoc) and (board.get(testLoc) == None or
                not board.get(testLoc).getColor() == color)):
            result.append(testLoc)
            if (board.get(testLoc)!=None):
                break
            curcol+=1
            testLoc = Location(currow, curcol)
        return result


#created by richard wang 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Rook(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("ROOK", "R", loc, brd, col, 5, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets possibleMovesArray
    def setPossibleMovesArray(self):
        board = self.getBoard()
        location = self.getLocation()
        col = self.getColor()
        playerCol = self.getPlayerCol()
        result = []
        currow = location.getRow()-1
        curcol = location.getCol()
        #up direction
        while (currow>0 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            currow -=1
        currow = location.getRow()+1
        #down direction
        while (currow<7 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            currow +=1
        currow = location.getRow()
        curcol = location.getCol()-1
        #left direction
        while (curcol>0 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            curcol-=1
        curcol = location.getCol()+1
        #right direction
        while (curcol<7 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            curcol+=1
        attacked = self.getAttackedPiecesArray()
        for p in attacked:
            result.append(p.getLocation())
        #finally
        super().setPossibleMovesArray(result)

    #sets attackedPiecesArray
    def setAttackedPiecesArray(self):
        board = self.getBoard()
        location = self.getLocation()
        col = self.getColor()
        playerCol = self.getPlayerCol()
        result = []
        currow = location.getRow()-1
        curcol = location.getCol()
        #up direction
        while (currow>0 and board.get(Location(currow,curcol))==None):
            currow -=1
        loc = Location(currow,curcol)
        if (board.isValid(loc) and board.get(loc)!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        currow = location.getRow()+1
        #down direction
        while (currow<7 and board.get(Location(currow,curcol))==None):
            currow +=1
        loc = Location(currow,curcol)
        if (board.isValid(loc) and board.get(loc)!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        currow = location.getRow()
        curcol = location.getCol()-1
        #left direction
        while (curcol>0 and board.get(Location(currow,curcol))==None):
            curcol-=1
        loc = Location(currow,curcol)
        if (board.isValid(loc) and board.get(loc)!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        curcol = location.getCol()+1
        #right direction
        while (curcol<7 and board.get(Location(currow,curcol))==None):
            curcol+=1
        loc = Location(currow,curcol)
        if (board.isValid(loc) and board.get(loc)!= None and
            not board.get(Location(currow,curcol)).getColor() == (col)):
            result.append(board.get(Location(currow,curcol)))
        super().setAttackedPiecesArray(result)



#created by richard wang 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Bishop(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("BISHOP", "B", loc, brd, col, 3, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets the attackedPiecesArray
    def setAttackedPiecesArray(self):
        board = self.getBoard()
        pos = self._getDiagonalLocations()
        result = []
        for l in pos:
            obj = board.get(l)
            if (obj!=None):
                result.append(obj)
        super().setAttackedPiecesArray(result)

    #sets the possibleMovesArray
    def setPossibleMovesArray(self):
        result = self._getDiagonalLocations()
        super().setPossibleMovesArray(result)

    #gets valid locations diagonal to current position
    #also locations should not be balcked off
    def _getDiagonalLocations(self):
        result = []
        loc = self.getLocation()
        col = self.getColor()
        board = self.getBoard()
        currow = loc.getRow()
        curcol = loc.getCol()
        #top left
        currow-=1
        curcol-=1
        test = Location(currow, curcol)
        while (board.isValid(test) and (board.get(test) == None or
                not board.get(test).getColor()==col)):
            result.append(test)
            if (board.get(test)!=None):
                break
            currow-=1
            curcol-=1
            test = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom right
        currow+=1
        curcol+=1
        test = Location(currow, curcol)
        while (board.isValid(test) and (board.get(test) == None or
                not board.get(test).getColor() == col)):
            result.append(test)
            if (board.get(test)!=None):
                break
            currow+=1
            curcol+=1
            test = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #top right
        currow-=1
        curcol+=1
        test = Location(currow, curcol)
        while (board.isValid(test) and (board.get(test) == None or
                not board.get(test).getColor() == col)):
            result.append(test)
            if (board.get(test)!=None):
                break
            currow-=1
            curcol+=1
            test = Location(currow, curcol)
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom left
        currow+=1
        curcol-=1
        test = Location(currow, curcol)
        while (board.isValid(test) and (board.get(test) == None or
                not board.get(test).getColor() == col)):
            result.append(test)
            if (board.get(test)!=None):
                break
            currow+=1
            curcol-=1
            test = Location(currow, curcol)
        return result



import math
# Created by richardwang007 on 8/02/17
#overall structure and method ideas some taken from
#a tetris game created in java in AP CS and its framework, written by
#my teacher, Ms. King, but much added to that
class Location(object):
    #DO NOT MODIFY!!!!!
    #PUBLIC STATIC FINAL!!!! :P
    directions = {
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
    _Location__directions = directions

    #contructor for location
    #takes in a row and a col
    def __init__(self, r, c):
        self.row = r
        self.col = c

    #gets the row of a location object
    def getRow(self):
        return self.row

    #gets the col of a location object
    def getCol(self):
        return self.col

    #creates location string
    def __str__(self):
        return "(" + str(self.getRow()) + ", " + str(self.getCol()) + ")"

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
        adjustedDirection = ((direction + self.__directions["half_right"] / 2) %
                            self.__directions['full_circle'])
        if (adjustedDirection < 0):
            adjustedDirection += self.__directions['full_circle']
        adjustedDirection = ((adjustedDirection //
                            self.__directions['half_right']) *
                            self.__directions['half_right'])
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
        if (compassAngle < 0):
            compassAngle += self.__directions['full_circle']
        #round
        return ((compassAngle // self.__directions['half_right']) *
                self.__directions['half_right'])

    # compares two locations
    # returns -1 if self is less than other
    # 1 is self is greater than other
    # 0 if equal
    #like in java comparable LOL
    def compareTo(self, other):
        if(not isinstance(other, Location)):
            raise ValueError(other + "not location")
        if (self.getRow() < other.getRow()):
            return -1
        if (self.getRow() > otherLoc.getRow()):
            return 1
        if (self.getCol() < otherLoc.getCol()):
            return -1
        if (self.getCol() > otherLoc.getCol()):
            return 1
        return 0


#created by richard wang on 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class King(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("KING", "K", loc, brd, col, 2, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets the possibleMovesArray
    def setPossibleMovesArray(self):
        board = self.getBoard()
        color = self.getColor()
        pos = self._getBorderingLocations()
        attacked = self.getAttackedPiecesArray()
        for i in range(len(pos)-1, -1, -1):
            if (board.get(pos[i])!=None):
                pos.pop(i)
        for piece in attacked:
            pos.append(piece.getLocation())
        super().setPossibleMovesArray(pos)

    #sets attackedPiecesArray
    def setAttackedPiecesArray(self):
        board = self.getBoard()
        color = self.getColor()
        result = []
        pos = self._getBorderingLocations()
        for location in pos:
            if (board.get(location) != None and
                not board.get(location).getColor() == color):
                result.append(board.get(location))
        super().setAttackedPiecesArray(result)

    #returns list of bordering valid locations
    def _getBorderingLocations(self):
        current = self.getLocation()
        result = []
        board = self.getBoard()
        d = Location.directions
        result.append(current.getAdjacentLocation(d['north']))
        result.append(current.getAdjacentLocation(d['northeast']))
        result.append(current.getAdjacentLocation(d['east']))
        result.append(current.getAdjacentLocation(d['southeast']))
        result.append(current.getAdjacentLocation(d['south']))
        result.append(current.getAdjacentLocation(d['southwest']))
        result.append(current.getAdjacentLocation(d['west']))
        result.append(current.getAdjacentLocation(d['northwest']))
        for i in range(len(result)-1, -1, -1):
            if (not board.isValid(result[i])):
                result.pop(i)
        return result



#created by richard wang on 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Knight(Piece):
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("KNIGHT", "N", loc, brd, col, 3, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets attackedPiecesArray
    def setAttackedPiecesArray(self):
        result = []
        col = self.getColor()
        board = self.getBoard()
        possible = self._getJumpPossibilities()
        for i in range(0, len(possible)):
            cur = possible[i]
            curPiece = board.get(cur)
            if (curPiece!=None and not curPiece.getColor() == col):
                result.append(curPiece)
        super().setAttackedPiecesArray(result)

    #sets possibleMovesArray
    def setPossibleMovesArray(self):
        result = []
        col = self.getColor()
        board = self.getBoard()
        possible = self._getJumpPossibilities()
        for loc in possible:
            curPiece = board.get(loc)
            if (curPiece == None or not curPiece.getColor() == col):
                result.append(loc)
        super().setPossibleMovesArray(result)

    #gets all valid locations for knight jumps
    #from current location
    def _getJumpPossibilities(self):
        result = []
        loc = self.getLocation()
        board = self.getBoard()
        currow = loc.getRow()
        curcol = loc.getCol()
        for i in range(-2,3):
            if (abs(i) == 1):
                currow += i
                left = Location(currow, curcol - 2)
                curcol = loc.getCol()
                right = Location(currow, curcol + 2)
                if (board.isValid(left)):
                    result.append(left)
                if (board.isValid(right)):
                    result.append(right)
            elif (abs(i) == 2):
                currow += i
                left = Location(currow, curcol - 1)
                curcol = loc.getCol()
                right = Location(currow, curcol + 1)
                if (board.isValid(left)): result.append(left)
                if (board.isValid(right)): result.append(right)
            currow = loc.getRow()
        return result


#created by richard wang on 08/07/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Pawn(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("PAWN", "", loc, brd, col, 1, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets the attackedPiecesArray
    def setAttackedPiecesArray(self): ####DONT FORGET TO ADD EN PASSANT LATER
        board = self.getBoard()
        location = self.getLocation()
        color = self.getColor()
        playerCol = self.getPlayerCol()
        dirs = Location.directions
        attacked = []
        if (board.isValid(location.getAdjacentLocation(dirs['northeast']))):
            adjNorthEast=board.get(
                            location.getAdjacentLocation(dirs['northeast']))
        else: adjNorthEast = None
        if (board.isValid(location.getAdjacentLocation(dirs['northwest']))):
            adjNorthWest=board.get(
                            location.getAdjacentLocation(dirs['northwest']))
        else: adjNorthWest = None
        if (board.isValid(location.getAdjacentLocation(dirs['southwest']))):
            adjSouthWest=board.get(
                            location.getAdjacentLocation(dirs['southwest']))
        else: adjSouthWest = None
        if (board.isValid(location.getAdjacentLocation(dirs['southeast']))):
            adjSouthEast=board.get(
                            location.getAdjacentLocation(dirs['southeast']))
        else: adjSouthEast = None
        if (not playerCol == color):
            if (adjSouthEast !=None and playerCol == (adjSouthEast.getColor())):
                attacked.append(adjSouthEast)
            if (adjSouthWest !=None and playerCol == (adjSouthWest.getColor())):
                attacked.append(adjSouthWest)
        else:
            if (adjNorthEast !=None and playerCol != (adjNorthEast.getColor())):
                attacked.append(adjNorthEast)
            if (adjNorthWest !=None and playerCol!=(adjNorthWest.getColor())):
                attacked.append(adjNorthWest)
        super().setAttackedPiecesArray(attacked)

    #sets possibleMovesArray
    def setPossibleMovesArray(self):  #ADD ENPASSANT
        board = self.getBoard()
        location = self.getLocation()
        col = self.getColor()
        dirs = Location.directions
        possible = []
        adjSouth = board.get(location.getAdjacentLocation(dirs['south']))
        adjNorth = board.get(location.getAdjacentLocation(dirs['north']))
        playerCol = self.getPlayerCol()
        #determines by player color
        if (playerCol == (col)):
            if (adjNorth == None):
                initialJump = location.getAdjacentLocation(
                    dirs['north']).getAdjacentLocation(dirs['north'])
                if (location.getRow() == 6 and board.get(initialJump)==None):
                    possible.append(initialJump)
                possible.append(location.getAdjacentLocation(dirs['north']))
        else:
            if (adjSouth == None):
                initialJump = location.getAdjacentLocation(
                    dirs['south']).getAdjacentLocation(dirs['south'])
                if (location.getRow() == 1 and board.get(initialJump)==None):
                    possible.append(initialJump)
                possible.append(location.getAdjacentLocation(dirs['south']))
        #goes through attacked pieces
        attacked = self.getAttackedPiecesArray()
        for piece in attacked:
            possible.append(piece.getLocation())
        super().setPossibleMovesArray(possible)


#created richard wang 08/06/17
class Display(object):
    #constructor
    def __init__(self, brd, playerColor, isWhite, ai):
        self.width = 800
        self.height = 800
        self.board = brd
        self.playerCol = playerColor;
        self.playerIsWhite = isWhite;
        self.pieceSelected = False
        self.selectedPiece = None
        self.gridExtraColors = [x[:] for x in [[None]*(self.board.getNumCols()+2)]*(self.board.getNumRows()+2)]
        #its +2 because that makes a balanced square
        #there'll be a border around the board
        self.grid = [x[:] for x in 
        [[None]*(self.board.getNumCols()+2)]*(self.board.getNumRows()+2)]
        self.turnOver = False
        self.whiteChecked = False
        self.blackChecked = False
        self.isWhiteTurn = True
        self.gameOver = False
        self.isAI = ai
        

    #dict of imagenames
    def imagesInit(self):
        images = {"WPAWN" : PhotoImage(file = 'WPAWN.gif'),
                "WROOK" : PhotoImage(file = "WROOK.gif"), 
                "WKNIGHT": PhotoImage(file = "WKNIGHT.gif"), 
                "WBISHOP": PhotoImage(file = "WBISHOP.gif"),
                "WQUEEN" : PhotoImage(file = "WQUEEN.gif"), 
                "WKING": PhotoImage(file = "WKING.gif"), 
                "BPAWN": PhotoImage(file = "BPAWN.gif"),
                "BROOK": PhotoImage(file = "BROOK.gif"),
                "BKNIGHT" : PhotoImage(file = "BKNIGHT.gif"), 
                "BBISHOP" : PhotoImage(file = "BBISHOP.gif"),
                "BQUEEN": PhotoImage(file = "BQUEEN.gif"), 
                "BKING": PhotoImage(file = "BKING.gif")}
        for key in images:
            #scaleH = int(pic.height()//(colSize-3) + 1)
            #scaleW = int(pic.width()//(rowSize-3) + 1)
            images[key] = images[key].subsample(2,2)
        return images

    #interface from course website
    def mousePressed(self, event=None, x=None, y=None):
        if (not self.gameOver):
            if (event!=None): row, col = self.getMouseClick(event.x, event.y)
            else: row, col = self.getMouseClick(x, y)
            row-=1
            col-=1
            location = Location(row, col)
            print(self.selectedPiece)
            if (self.pieceSelected):
                curLoc = self.selectedPiece.getLocation()
                copy = self.board.copy()
                if (self.selectedPiece.move(location) != False):
                    self.updatePieces()
                    #print("handleMate 1")
                    #self.handleMate()
                    self.blackChecked = self.board.blackInCheck()
                    self.whiteChecked = self.board.whiteInCheck()
                    if ((self.isWhiteTurn and self.whiteChecked) or 
                        (not self.isWhiteTurn and self.blackChecked)):
                        self.board = copy.copy()
                        #self.updatePieces()
                        #print("handleMate 2")
                        #self.handleMate()
                    else:
                        self.pieceSelected = False
                        self.selectedPiece = None
                        self.turnOver = True
                        self.isWhiteTurn = not self.isWhiteTurn
                        #self.updatePieces()
                        #self.handleMate()
                    self.updatePieces()
                    print("handle")
                    self.handleMate()
                elif(self.board.isValid(location) and 
                    self.board.get(location)!=None and 
                    self.board.get(location).getColor() ==
                    self.selectedPiece.getColor()):
                    self.selectedPiece = self.board.get(location)
                    print(self.selectedPiece)
                    for loc in self.selectedPiece.getPossibleMovesArray():
                        print(loc)
                else:
                    self.pieceSelected = False
                    self.selectedPiece = None
            else:
                if (self.board.isValid(location)):
                    piece = self.board.get(location)
                    if (piece != None):
                        if ((self.isWhiteTurn and piece.getColor()=='white') or
                        (not self.isWhiteTurn and piece.getColor()=='black')):
                            print(piece)
                            for loc in piece.getPossibleMovesArray():
                                print(loc)
                            self.selectedPiece = piece
                            self.pieceSelected = True


    #handles the checks and mates
    def handleMate(self):
        self.blackChecked = self.board.blackInCheck()
        self.whiteChecked = self.board.whiteInCheck()
        if (self.board.whiteInCheckmate() or self.board.blackInCheckmate()):
            self.gameOver = True
            print("checkmate")
    
    #updates the arrays for the different pieces
    def updatePieces(self):
        for loc in self.board.getOccupiedLocations():
            p = self.board.get(loc)
            p.setAttackedPiecesArray()
            p.setPossibleMovesArray()
    
    
    
    #handles draggin of mouse
    def mouseDragged(self, event):
        pass


    #idea from my snake implementation
    def getMouseClick(self, x,y):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                w = self.width
                h = self.height
                cellW = w / len(self.grid[row])
                cellH = h / len(self.grid)
                x0 = cellW * col
                y0 = cellH * row
                x1 = cellW * (col + 1)
                y1 = cellH * (row + 1)
                if (x<=x1 and x>=x0 and y<=y1 and y>=y0):
                    return (row,col)
        return (0,0)

    #taken from the 15112 course website
    def redrawAllWrapper(self, canvas):
        canvas.delete(ALL)
        self.displayBoard(canvas)
        canvas.update()

    #taken from the 15112 course website example
    def mouseEventWrapper(self, event, canvas):
        if (self.isAI):
            if ((self.playerIsWhite and self.isWhiteTurn) or 
                (not self.playerIsWhite and not self.isWhiteTurn)):
                self.mousePressed(event)
                self.redrawAllWrapper(canvas)
        else:
            self.mousePressed(event)
            self.redrawAllWrapper(canvas)
        #else:
            #result = self.rootNegaMax(3,self.isWhiteTurn)
            #x1, y1 = self.locationToMouseClick(result[1])
            #loc = result[0].getLocation()
            #x0,y0 = self.locationToMouseClick(loc)
            #self.mousePressed(event = None, x = x0, y = y0)
            #self.mousePressed(event = None, x = x1, y = y1)
            
    #calls ai
    def timerFiredWrapper(self, canvas):
        if (not ((self.playerIsWhite and self.isWhiteTurn) or 
            (not self.playerIsWhite and not self.isWhiteTurn))):
            result = self.rootNegaMax(2,self.isWhiteTurn)
            x1, y1 = self.locationToMouseClick(result[1])
            loc = result[0].getLocation()
            x0,y0 = self.locationToMouseClick(loc)
            print("******************************")
            print(self.getMouseClick(x0-1,y0-1))
            print(self.getMouseClick(x1-1,y1-1))
            print("*****************************")
            self.mousePressed(event = None, x = x0, y = y0)
            self.mousePressed(event = None, x = x1, y = y1)
            self.redrawAllWrapper(canvas)
        canvas.after(self.timerDelay, self.timerFiredWrapper, canvas)
    
    #creates the cavnas and shows it
    def createGUI(self):
        master = Tk()
        self.master = master
        canvas = Canvas(master, width = self.width, height = self.height)
        canvas.pack()
        self.timerDelay = 1000
        self.images = self.imagesInit()
        self.displayBoard(canvas)
        master.bind("<Button-1>", 
            lambda event: self.mouseEventWrapper(event, canvas))
        if (self.isAI):
            self.timerFiredWrapper(canvas)
        #canvas.bind("<B1-Motion>",
            #lambda event: self.mouseEventWrapper(mouseDragged, event, canvas))
        mainloop()

    #displays the board
    def displayBoard(self, canvas):
        rowSize = self.height/len(self.grid)
        colSize = self.width/len(self.grid[0])
        x0, y0 = 0,0
        x1, y1 = colSize, rowSize
        for row in range(len(self.grid)):
            x0, x1 = 0, colSize
            for col in range(len(self.grid[row])):
                #border
                if ((col+row) % 2 == 0): color = 'white'
                else: color = 'light slate grey'
                if (row == 0 or col == 0 or col == 9 or row == 9):
                    color = "PeachPuff4"
                canvas.create_rectangle(x0,y0,x1,y1,fill = color)
                x0 += colSize
                x1 += colSize
            y0+=rowSize
            y1+=rowSize
        self.showPieces(canvas)


    #shows the pieces on the board
    def showPieces(self, canvas):
        rowSize = self.height/len(self.grid)
        colSize = self.width/len(self.grid[0])
        x0, y0 = colSize, rowSize
        halfX = colSize/2
        halfY = rowSize/2
        for row in range(self.board.getNumRows()):
            x0 = colSize
            for col in range(self.board.getNumCols()):
                if (self.board.isValid(Location(row, col))):
                    piece = self.board.get(Location(row, col));
                    if (piece != None):
                        name = piece.getImageFileName()
                        canvas.create_image(x0 + halfX,y0 + halfY,
                                            image = self.images[name])
                x0 += colSize
            y0+=rowSize

                                                            
    #a negaMax algorithm, pseudo code on 
    #changed to tuple format to fit piece, move
    #https://chessprogramming.wikispaces.com/Negamax
    def negaMax(self, depth, whiteTurn):
        if (depth ==0):
            return self.evaluateValue()
        max = -float('Inf')
        if (whiteTurn): color = 'white'
        else: color = 'black'
        #copies board position
        copy = self.board.copy()
        for loc in self.board.getOccupiedLocations():
            piece = self.board.get(loc)
            if (piece != None and piece.getColor() == color):
                for move in self.board.get(loc).getPossibleMovesArray():
                    self.board.get(loc).moveTo(move)
                    if ((whiteTurn and self.board.whiteInCheck()) or
                        (not whiteTurn and self.board.blackInCheck())):
                        self.board = copy.copy()
                        continue
                    value = -self.negaMax(depth -1, not whiteTurn)
                    if(value >= max):
                        max = value
                    self.board = copy.copy()
                    self.updatePieces()
        return max
        
    #root negaMax because I cant figure this out otherwise
    def rootNegaMax(self, depth, whiteTurn):
        print("nega start")
        result = None
        max = -float('Inf')
        if (whiteTurn): color = 'white'
        else: color = 'black'
        #copies board position
        copy = self.board.copy()
        for loc in self.board.getOccupiedLocations():
            piece = self.board.get(loc)
            print(piece)
            if (piece != None and piece.getColor() == color):
                for move in self.board.get(loc).getPossibleMovesArray():
                    print(loc.getRow(), loc.getCol())
                    self.board.get(loc).moveTo(move)
                    #does not recognize check and checkmate
                    #attempts to play moves that would result in 
                    #it being in check
                    #need to prune all branches with self inflicting checks
                    if ((whiteTurn and self.board.whiteInCheck()) or
                        (not whiteTurn and self.board.blackInCheck())):
                        self.board = copy.copy()
                        continue
                    value = -self.negaMax(depth -1, not whiteTurn)
                    print("nega value: "+str(value))
                    print(self.board.get(loc))
                    print(move)
                    self.board = copy.copy()
                    self.updatePieces()
                    if(value >= max):
                        max = value
                        result = (self.board.get(loc), move)
                    self.updatePieces()
                    
        print("nega")
        print(result[0])
        print(result[1])
        print("nega done")
        return result
        
        
    #evaluates the value of the board
    #idea taken from https://chessprogramming.wikispaces.com/Negamax
    def evaluateValue(self):
        neg = 1 if self.isWhiteTurn else -1
        if (self.board.whiteInCheckmate() or 
            self.board.blackInCheckmate()):
            return neg * -1 * float('Inf')
        wVal = self.board.whiteMaterialValue()
        bVal = self.board.blackMaterialValue()
        return (wVal - bVal) * neg
        
    #takes location and turns it into a mouse x and y
    def locationToMouseClick(self, location):
        r = location.getRow()
        c = location.getCol()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if (row-1 ==r and col-1 == c):
                    w = self.width
                    h = self.height
                    cellW = w / len(self.grid[row])
                    cellH = h / len(self.grid)
                    halfW = cellW/2
                    halfH = cellH/2
                    x0 = cellW * col
                    y0 = cellH * row
                    x1 = cellW * (col + 1)
                    y1 = cellH * (row + 1)
                    return (x0 + halfW, y0 + halfH)
        return (0,0)
        
        

#Created by richardwang007 on 8/02/17
#overall structure and method ideas some taken from
#a tetris game created in java in AP CS and its framework, written by
#my teacher, Ms. King, but much added to that
class BoardArray(object):

    # makes the board of row and col length
    def __init__(self, rows, cols):
        self.board = [x[:] for x in [[None]*cols]*rows]



    #returns a copy
    def copy(self):
        copy = BoardArray(self.getNumRows(), self.getNumCols())
        for location in self.getOccupiedLocations():
            curPiece = self.get(location)
            if (type(curPiece) == Pawn):
                new = Pawn(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            elif(type(curPiece) == Rook):
                new = Rook(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            elif(type(curPiece) == Bishop):
                new = Bishop(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            elif(type(curPiece) == Knight):
                new = Knight(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            elif(type(curPiece) == Queen):
                new = Queen(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            elif(type(curPiece) == King):
                new = King(curPiece.location,copy,
                            curPiece.color,curPiece.playerCol)
            copy.put(location, new)
        return copy

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
            raise ValueError("Location " + str(loc)
                    + " is not valid")
        return self.board[loc.getRow()][loc.getCol()]

    #Puts an object in a selected location on the grid
    #returns the object previously occupying the location
    #or None if the location was empty
    def put(self, loc, obj):
        if (not self.isValid(loc)):
            raise ValueError("Location " + str(loc)
                    + " is not valid")
        if (obj == None):
            raise ValueError("Object is None")
        removed = self.get(loc)
        self.board[loc.getRow()][loc.getCol()] = obj
        return removed

    #removes the element at the location on the grid
    #then returns that element
    #returns None if that location is empty
    def remove(self, loc):
        if (not self.isValid(loc)):
            raise ValueError("Location " + str(loc)
                    + " is not valid")
        removed = self.get(loc)
        self.board[loc.getRow()][loc.getCol()] = None
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

    #updates the arrays for the different pieces
    def updatePieces(self):
        for loc in self.getOccupiedLocations():
            p = self.get(loc)
            p.setAttackedPiecesArray()
            p.setPossibleMovesArray()
    
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
        
    #returns all black pieces
    def getBlackPieces(self):
        locations = self.getOccupiedLocations()
        result = []
        for loc in locations:
            piece = self.get(loc)
            if (piece.getColor() == "black"):
                result.append(piece)
        return result
        
    #returns all white pieces
    def getWhitePieces(self):
        locations = self.getOccupiedLocations()
        result = []
        for loc in locations:
            piece = self.get(loc)
            if (piece.getColor() == "white"):
                result.append(piece)
        return result
        
    #gets white possible moves
    def getPossibleWhiteMoves(self):
        pieces = self.getWhitePieces()
        result = []
        for piece in pieces:
            result+=piece.getPossibleMovesArray()
        return result
        
    #gets black possible moves
    def getPossibleBlackMoves(self):
        pieces = self.getBlackPieces()
        result = []
        for piece in pieces:
            result += piece.getPossibleMovesArray()
        return result
    
    #gets black king location
    def getBlackKingLocation(self):
        locations = self.getOccupiedLocations()
        for loc in locations:
            piece = self.get(loc)
            if (piece.getColor() == "black" and type(piece) == King):
                return loc
                
    #gets white king location
    def getWhiteKingLocation(self):
        locations = self.getOccupiedLocations()
        for loc in locations:
            piece = self.get(loc)
            if (piece.getColor() == "white" and type(piece) == King):
                return loc
                
    
    #gets if white king is in check
    def whiteInCheck(self):
        whiteKingLocation = self.getWhiteKingLocation()
        bPurview = self.getPossibleBlackMoves()
        for loc in bPurview:
            if (whiteKingLocation == loc):
                return True
        return False
        
    #gets if black king is in check
    def blackInCheck(self):
        blackKingLocation = self.getBlackKingLocation()
        wPurview = self.getPossibleWhiteMoves()
        for loc in wPurview:
            if(blackKingLocation == loc):
                return True
        return False
        
        
    #finds if white is in checkmate
    def whiteInCheckmate(self):
        if (self.whiteInCheck()):
            copy = self.copy()
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    p = self.get(Location(row,col))
                    print("**********")
                    print(p)
                    if (p != None and p.getColor() == 'white'):
                        for moves in p.getPossibleMovesArray():
                            print(moves)
                            self.get(Location(row,col)).move(moves)
                            self.updatePieces()
                            if(not self.whiteInCheck()):
                                self.board = copy.copy().board
                                self.updatePieces()
                                return False
                            self.board = copy.copy().board
                            self.updatePieces()
            return True
        return False
        #HEYHEY
        #if you are reading this, these look exactly the same but aren't
        #kms
        '''
        if (self.whiteInCheck()):
            copy = self.copy()
            for piece in self.getWhitePieces():
                for moves in piece.getPossibleMovesArray():
                    piece.move(moves)
                    self.updatePieces()
                    if(not self.whiteInCheck()):
                        self.board = copy.copy().board
                        self.updatePieces()
                        return False
                    self.board = copy.copy().board
                    self.updatePieces()
            return True
        return False
        '''
        '''
        if (self.whiteInCheck()):
            whiteKingLocation = self.getWhiteKingLocation()
            whiteKing = self.get(whiteKingLocation)
            copy = self.copy()
            pieces = self.getWhitePieces()
            for piece in pieces:
                for moves in piece.getPossibleMovesArray():
                    piece.move(moves)
                    self.updatePieces()
                    if (not self.whiteInCheck()):
                        self.board = copy.copy().board
                        self.updatePieces()
                        return False
                    self.board = copy.copy().board
            #self.board = copy.copy().board
            self.updatePieces()
            return True
        return False
        '''
        
    #find if black is in checkmate
    def blackInCheckmate(self):
        if (self.blackInCheck()):
            copy = self.copy()
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    p = self.get(Location(row,col))
                    print("**********")
                    print(p)
                    if (p != None and p.getColor() == 'black'):
                        for moves in p.getPossibleMovesArray():
                            print(moves)
                            self.get(Location(row,col)).move(moves)
                            self.updatePieces()
                            if(not self.blackInCheck()):
                                self.board = copy.copy().board
                                self.updatePieces()
                                return False
                            self.board = copy.copy().board
                            self.updatePieces()
            return True
        return False
        '''
            for piece in self.getBlackPieces():
                print("**********")
                print(piece)
                for moves in piece.getPossibleMovesArray():
                    print(moves)
                    piece.move(moves)
                    self.updatePieces()
                    if(not self.blackInCheck()):
                        self.board = copy.copy().board
                        self.updatePieces()
                        return False
                    self.board = copy.copy().board
                    self.updatePieces()
            return True
        return False
        '''
        '''
            blackKingLocation = self.getBlackKingLocation()
            blackKing = self.get(blackKingLocation)
            copy = self.copy()
            pieces = self.getBlackPieces()
            for piece in pieces:
                for moves in piece.getPossibleMovesArray():
                    piece.move(moves)
                    self.updatePieces()
                    if (not self.blackInCheck()):
                        self.board = copy.copy().board
                        self.updatePieces()
                        return False
                    self.board = copy.copy().board
            #self.board = copy.copy().board
            self.updatePieces()
            return True
        return False
        '''
    
    #sum white pieces material value
    def whiteMaterialValue(self):
        result = 0
        for piece in self.getWhitePieces():
            result+=piece.getValue()
        return result
        
    #sum black pieces material value
    def blackMaterialValue(self):
        result = 0
        for piece in self.getBlackPieces():
            result += piece.getValue()
        return result


#created by
class Chess(object):
    #constructor
    def __init__(self, color, playerIsWhite, isAI):
        #self.moveAndFENList = MoveAndFENList()
        self.boardArray = BoardArray(8,8)
        self.playerColor = color
        self.otherColor = 'white' if color == 'black' else 'black'
        self.isWhite = playerIsWhite
        self.boardDisplay = Display(self.boardArray,
                                        self.playerColor, self.isWhite, isAI)
        self.initialBoardPosition(self.boardArray)
        

    #case-by-case initialization of starting position of board
    def initialBoardPosition(self,board):
        for row in {0,1,6,7}:
            for col in range(board.getNumCols()):
                loc = Location(row,col)
                if (row == 1):
                    board.put(loc, Pawn(loc, board,
                                    self.otherColor, self.playerColor))
                elif(row == 6):
                    board.put(loc, Pawn(loc, board,
                                    self.playerColor, self.playerColor))
                elif(col == 0 or col == 7):
                    if (row == 0):
                        board.put(loc, Rook(loc, board, self.otherColor,
                                                        self.playerColor))
                    elif(row==7):
                        board.put(loc, Rook(loc, board, self.playerColor,
                                                        self.playerColor))
                elif (col == 1 or col == 6):
                    if (row == 0):
                        board.put(loc, Knight(loc, board, self.otherColor,
                                                            self.playerColor))
                    elif(row == 7):
                        board.put(loc, Knight(loc, board, self.playerColor,
                                                            self.playerColor))
                elif(col == 2 or col == 5):
                    if (row == 0):
                        board.put(loc, Bishop(loc,board,self.otherColor,
                                                        self.playerColor))
                    if(row == 7):
                        board.put(loc, Bishop(loc,board,self.playerColor,
                                                        self.playerColor))
                #the king and queen arent the same row and col
                #when the player color is different
                #so they are annoying
                elif(col == 3 or col == 4):
                    if(self.playerColor == 'white'):
                        if (col == 4):
                            if (row == 0):
                                board.put(loc, King(loc,board,self.otherColor,
                                                            self.playerColor))
                            elif(row == 7):
                                board.put(loc, King(loc, board,self.playerColor,
                                                            self.playerColor))
                        elif(col == 3):
                            if(row ==0):
                                board.put(loc, Queen(loc,board,self.otherColor,
                                                            self.playerColor))
                            elif(row == 7):
                                board.put(loc, Queen(loc,board,self.playerColor,
                                                            self.playerColor))
                    elif(self.playerColor == 'black'):
                        if (col == 4):
                            if (row == 0):
                                board.put(loc, Queen(loc,board,self.otherColor,
                                                            self.playerColor))
                            elif(row == 7):
                                board.put(loc, Queen(loc,board,self.playerColor,
                                                            self.playerColor))
                        elif(col == 3):
                            if(row ==0):
                                board.put(loc, King(loc,board,self.otherColor,
                                                            self.playerColor))
                            elif(row == 7):
                                board.put(loc, King(loc,board,self.playerColor,
                                                            self.playerColor))
                                                            
        self.boardDisplay.updatePieces()
                                
    
    #plays through a game
    def playGame(self):
        pass
    
    
    
    def main(self):
        self.boardDisplay.createGUI()
        

    

#draws the Input UI
def drawInput(canvas):
    canvas.create_text(133,200,font = 'Times 30', text='Play White\nAgainst AI')
    canvas.create_rectangle(266,0,532,800,fill='black')
    canvas.create_text(399,200,font='Times 30',fill='white',
                        text="Play Black\nAgainst AI")
    canvas.create_rectangle(532,0,800,800,fill = 'light slate grey')
    canvas.create_text(665,200,font = 'Times 30', fill = 'peach puff',
                        text = 'Play With Friend')

def picker(event, root, color):
    x,y = event.x,event.y
    if (x<266 and y>0 and y<800):
        color.append('white')
        root.destroy()
    if(x>266 and x<532 and y>0 and y<800):
        color.append('black')
        root.destroy()
    if(x>532 and y>0 and y<800):
        color.append('friend')
        root.destroy()
    

root = Tk()
c = Canvas(root, width = 800, height = 800)
c.pack()
drawInput(c)
color = []
root.bind("<Button-1>", lambda event: picker(event, root, color))
root.mainloop()
if (len(color)>0 and color[0] == 'white'):
    c = Chess('white', True, True)
    c.main()
elif (len(color)>0 and color[0] == 'black'):
    c = Chess('black', False, True)
    c.main()
elif(len(color)>0 and color[0] == 'friend'):
    c = Chess('white', True, False)
    c.main()


