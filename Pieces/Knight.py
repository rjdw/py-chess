import ../Foundation/Location
import ../Foundation/BoardArray
import Piece

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
            if (curPiece == None || not curPiece.getColor() == col):
                result.append(cur)
        super().setPossibleMovesArray(result)

    #gets all valid locations for knight jumps
    #from current location
    def _getJumpPossibilities(self):
        result = []
        loc = self.getLocation()
        board = self.getBoard()
        currow = loc.getRow()
        curcol = loc.getCol()
        for i in range(-2,2):
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
