import ../Foundation/Location
import ../Foundation/BoardArray

#created by richard wang on 8/05
#got ideas for structure and implementation from
#pieces I wrote in java previously
class Piece(object):

    #constructor for piece
    def __init__(self, pieceName, note, loc, brd, col, val, plCol):
        #instance variables
        self.imageFileName = pieceName +".gif"
        self.possibleMovesArray=[]
        self.attackedPiecesArray = []
        self.board = brd
        self.location = loc
        self.color = col
        self.value = val
        self.notation = note
        self.playerCol = plCol
        self.imageFileName += "W" if self.playerCol == "white" else "B"


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
    def getValue(): return self.value

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
        return self.pieceName

    def __eq__(self, other):
        return type(self) == type(other)

    #removes self from its board
    def removeSelfFromGrid(self):
        if (self.board == None):
            raise Exception('peice not in a board')
        if (self.board.get(self.location) != self):
            raise Exception('piece no in' + str(self.location))
        self.board.remove(location)
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
        self.board.remove(location)
        occupant = self.board.get(newLocation)
        if (occupant != None):
            occupant.removeSelfFromGrid()
        self.location = newLocation
        self.board.put(location, self)
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
