import ../Foundation/Location
import ../Foundation/BoardArray
import Piece

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
        col = self.getColor()
        board = self.getBoard()
        currow = loc.getRow()
        curcol = loc.getCol()
        #top left
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow-=1
            curcol-=1
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom right
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow+=1
            curcol+=1
        currow = loc.getRow()
        curcol = loc.getCol()
        #top right
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor()==col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow-=1
            curcol+=1
        currow = loc.getRow()
        curcol = loc.getCol()
        #bottom left
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow+=1
            curcol-=1
        currow = loc.getRow()
        curcol = loc.getCol()
        #straight down
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow+=1
        currow = loc.getRow()
        #straight up
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            currow-=1
        currow = loc.getRow()
        #straight left
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            curcol-=1
        curcol = loc.getCol()
        #straight right
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
            pos = Location(currow, curcol)
            result.append(pos)
            if (board.get(pos)!=None):
                break
            curcol+=1
        return result
