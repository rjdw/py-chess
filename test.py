'''
from tkinter import *

        
def displayBoard(canvas):
    rowSize = 800/10
    colSize = 800/10
    x0, y0 = 0,0
    x1, y1 = colSize, rowSize
    for row in range(10):
        x0, x1 = 0, colSize
        for col in range(10):
            #border
            if ((col+row) % 2 == 0): color = 'white'
            else: color = 'black'
            if (row == 0 or col == 0 or col == 9 or row == 9):
                color = "light slate grey"
            canvas.create_rectangle(x0,y0,x1,y1,fill = color)
            x0 += colSize
            x1 += colSize
        y0+=rowSize
        y1+=rowSize
    showPieces(canvas)
    



#shows the pieces on the board
def showPieces(canvas):
    rowSize = 80
    colSize = 80
    x0, y0 = colSize, rowSize
    halfX = colSize/2
    halfY = rowSize/2
    pics = []
    for row in range(8):
        x0 = colSize 
        for col in range(8):
            pic = PhotoImage(file = "WKING.gif")
            scaleH = int(pic.height()//(colSize-3) + 1)
            scaleW = int(pic.width()//(rowSize-3) + 1)
            pic = pic.subsample(scaleW,scaleH)
            pics.append(pic)
            canvas.create_image(x0+halfX,y0+halfY, image = pic)
            x0 += colSize
        y0+=rowSize
    print(pics)
        

def tester(canvas):
    canvas.create_image(400,400, image = PhotoImage(file = "WKING.gif"))



master = Tk()
canvas = Canvas(master, width = 800, height = 800)
canvas.pack()
#showPieces(canvas)
#master.bind("<Button-1>", lambda event: mouse(event))
#canvas.create_rectangle(0,0,800,800,fill = 'yellow')
pics = [PhotoImage(file = "WKING.gif")]
#pic = pic.zoom(20)

#pic = pic.subsample(2)
canvas.create_image(400,400,image = pics[0])
mainloop()
'''
print("ok")
for i in range(10):
    print(i)
    if (i == 4): break

