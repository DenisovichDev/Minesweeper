from cell import *
import random

l = 40
mineNum = 30
grid = []
rows, cols = 0, 0
def setup():
    global grid, rows, cols, l, mineNum
    size(601, 601)
    cols = int(height / l)
    rows = int(width / l)
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(Cell(i, j, l))
            
    chosen = []
    for i in range(mineNum):
        while True:
            indexX = random.randint(0, rows - 1)
            indexY = random.randint(0, cols - 1)
            if (indexX, indexY) not in chosen: 
                grid[indexX][indexY].mine = True
                chosen.append((indexX, indexY))
            else:
                continue
            break
    
    for i in range(rows):
        for j in range(cols):
            grid[i][j].countBombs(grid, rows, cols)
            
def mousePressed():
    global rows, cols, grid
    
    for row in grid:
        for cell in row:
            if cell.confirm() and mouseButton == LEFT and not cell.flagged:
                if not cell.mine:
                    cell.reveal()
                elif cell.mine:
                    revealAll()
            elif cell.confirm() and mouseButton == RIGHT:
                if not cell.flagged:
                    cell.flag()
                elif cell.flagged:
                    cell.unflag()
                    cell.revealed = False
       
            
            # if cell.flood == True:
            #     cell.floodFill(grid, rows, cols)


def revealAll():
    global grid
    for row in grid:
        for cell in row:
            cell.reveal()
            if cell.flagged and (not cell.mine):
                cell.wrongOne = True
            

                
def draw():
    global grid, rows, cols
    background(255)
    
    for row in grid:
        for cell in row:
            cell.show()
            
            if cell.flood == True:
                cell.floodFill(grid, rows, cols)
