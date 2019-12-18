import ../Foundation/Location
import ../Foundation/BoardArray
import Piece

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
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor()==col):
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
            currow+=1
            curcol+=1
        currow = loc.getRow()
        curcol = loc.getCol()
        #top right
        while (board.isValid(Location(currow, curcol)) and
                not board.get(Location(currow, curcol)).getColor() == col):
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
        return result
