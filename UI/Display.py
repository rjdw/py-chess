from ..Foudation import BoardArray
from Tkinter import *
#created richard wang 08/06/17
class Display(object):
    #constructor
    def __init__(self, brd, playerColor, isWhite):
        self.width = 800
        self.height = 800
        self.board = brd
        self.playerCol = playerColor;
        self.playerIsWhite = isWhite;
        self.pieceSelected = False
        self.selectedPiece = None
        self.gridExtraColors = [x[:] for x in [[None]*self.board.getNumCols()+2]*self.board.getNumRows()+2]
        #its +2 because that makes a balanced square
        #there'll be a border around the board
        self.grid = [x[:] for x in [[None]*self.board.getNumCols()+2]*self.board.getNumRows()+2]


    #interface from course website
    def mousePressed(self, event):
        row, col = self.getMouseClick(event.x, event.y)
        location = Location(row, col)
        if (self.pieceSelected):
            self.selectedPiece.move(location)
            self.pieceSelected = False
            self.selectedPiece = None
        else:
            if (self.board.isValid(location)):
                piece = self.board.get(location)
                if (piece != None):
                    self.selectedPiece = piece
                    self.pieceSelected = True



    #idea from my snake implementation
    def getMouseClick(x,y):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                w = self.width - 2
                h = self.height - 2
                cellW = w / len(self.grid[row])
                cellH = h / len(self.grid)
                x0 = cellW * col
                y0 = cellH * row
                x1 = cellW * (col + 1)
                y1 = cellH * (row + 1)
                if (x<=x1 and x>=x0 and y<=y1 and y>=y0):
                    return (row,col)

    #taken from the 15112 course website
    def redrawAllWrapper(self, canvas):
        canvas.delete(ALL)
        self.displayBoard(canvas)
        canvas.update()

    #taken from the 15112 course website example
    def mousePressedWrapper(self, event, canvas):
        self.mousePressed(event)
        self.redrawAllWrapper(canvas)

    #creates the cavnas and shows it
    def createGUI(self):
        root = Tk()
        canvas = Canvas(root, width = self.width, height = self.height)
        canvas.pack()
        root.bind("<Button-1>", lambda event:
                                self.mousePressedWrapper(event, canvas))
        self.displayBoard(canvas)

    def displayBoard(self, canvas):
        rowSize = self.height/self.board.getNumRows()
        colSize = self.width/self.board.getNumCols()
        x0, y0 = 0,0
        x1, y1 = colSize, rowSize
        white = True
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x0, x1 = 0, colSize
                #border
                color = "white" if white else "black"
                if (row == 0 or col == 0 or col == 9 or row == 9):
                    color = "light slate grey"
                canvas.create_rectangle(x0,y0,x1,y1,fill = color)
                if (color == "white" or color == "black"): white = not white
                x0 += colSize
                x1 += colSize
            y0+=rowSize
            y1+=rowSize
        self.showPieces(canvas)




    #shows the pieces on the board
    def showPieces(self, canvas):
        rowSize = self.height/self.board.getNumRows()
        colSize = self.width/self.board.getNumCols()
        x0, y0 = 0,0
        x1, y1 = colSize, rowSize
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                x0, x1 = 0, colSize
                piece = None
                if (self.board.isValid(Location(row, col))):
                    piece = board.get(Location(row, col));
                    pic = None
                    if (piece != None):
                        pic = PhotoImage(piece.getImageFileName())
                        canvas.create_image(x0,y0,x1,y1,image = pic)
                x0 += colSize
                x1 += colSize
            y0+=rowSize
            y1+=rowSize
