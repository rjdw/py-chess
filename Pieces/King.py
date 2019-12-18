import ../Foundation/Location
import ../Foundation/BoardArray
import Piece

#created by richard wang on 08/05/17
#got ideas for structure and implementation from
#pieces I wrote in java previously
class King(Piece):
    #constructor
    def __init__(self, loc, brd, col, playerCol):
        super().__init__("KING", "K", loc, brd, col, 9, playerCol)
        self.setAttackedPiecesArray()
        self.setPossibleMovesArray()

    #sets the possibleMovesArray
    def setPossibleMovesArray(self):
        board = self.getBoard()
        color = self.getColor()
        pos = self.getBorderingLocations()
        attacked = self.getAttackedPiecesArray()
        for i in range(eln(pos)-1, -1, -1):
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
        pos = self.getBorderingLocations()
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
        d = Location.__directions
        result.append(current.getAdjacentLocation(d['north']))
        result.append(current.getAdjacentLocation(d.['northeast']))
        result.append(current.getAdjacentLocation(Location.['east']))
        result.append(current.getAdjacentLocation(Location.['southeast']))
        result.append(current.getAdjacentLocation(Location.['south']))
        result.append(current.getAdjacentLocation(Location.['southwest']))
        result.append(current.getAdjacentLocation(Location.['west']))
        result.append(current.getAdjacentLocation(Location.['northwest']))
        for i in range(len(result)-1, -1, -1):
            if (not board.isValid(result[i])):
                result.pop(i)
        return result
