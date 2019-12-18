import ../Foundation/Location
import ../Foundation/BoardArray
import Piece
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
        while (currow>=0 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            currow -=1
        currow = location.getRow()+1
        #down direction
        while (currow<=7 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            currow +=1
        currow = location.getRow()
        curcol = location.getCol()-1
        #left direction
        while (curcol>=0 and board.get(Location(currow,curcol))==None):
            result.append(Location(currow, curcol))
            curcol-=1
        curcol = location.getCol()+1
        #right direction
        while (curcol<=7 and board.get(Location(currow,curcol))==None):
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
        while (currow>=0 and board.get(Location(currow,curcol))==None):
            currow -=1
        if (board.get(Location(currow,curcol))!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        currow = location.getRow()+1
        #down direction
        while (currow<=7 and board.get(Location(currow,curcol))==None):
            currow +=1
        if (board.get(Location(currow,curcol))!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        currow = location.getRow()
        curcol = location.getCol()-1
        #left direction
        while (curcol>=0 and board.get(Location(currow,curcol))==None):
            curcol-=1
        if (board.get(Location(currow,curcol))!= None and
            not board.get(Location(currow,curcol)).getColor() == col):
            result.append(board.get(Location(currow,curcol)))
        curcol = location.getCol()+1
        #right direction
        while (curcol<=7 and board.get(Location(currow,curcol))==None):
            curcol+=1
        if (board.get(Location(currow,curcol))!= None and
            not board.get(Location(currow,curcol)).getColor().equals(col)):
            result.append(board.get(Location(currow,curcol)))
        super().setAttackedPiecesArray(result)
