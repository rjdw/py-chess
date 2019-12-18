import ../Foundation.*


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
        col = self.getColor()
        playerCol = self.getPlayerCol()
        dirs = Location.__directions
        attacked = []
        adjNorthEast=board.get(location.getAdjacentLocation(dirs['northeast']));
        adjNorthWest=board.get(location.getAdjacentLocation(dirs['northwest']));
        adjSouthWest=board.get(location.getAdjacentLocation(dirs['southwest']));
        adjSouthEast=board.get(location.getAdjacentLocation(dirs['southeast']));
        if (not playerCol == col):
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
        dirs = Location.__directions
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
                possible.append(location.getAdjacentLocation(dirs['NORTH']))
        else:
            if (adjSouth == None):
                initialJump = location.getAdjacentLocation(
                    dirs.['south']).getAdjacentLocation(dirs['south'])
                if (location.getRow() == 1 and board.get(initialJump)==None):
                    possible.append(initialJump)
                possible.append(location.getAdjacentLocation(dirs.['south']))
        #goes through attacked pieces
        attacked = self.getAttackedPiecesArray()
        for piece in attacked:
            possible.append(piece.getLocation())
        super().setPossibleMovesArray(possible)
