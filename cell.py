class Cell(object):
    
    def __init__(self, row, col, l):
        self.row = row
        self.col = col
        self.l = l
        self.x = self.row * self.l
        self.y = self.col * self.l
        self.mine = False    
        self.revealed = False
        self.flagged = False
        self.wrongOne = False
        self.count = 0
        self.flood = False
        self.mineImg =loadImage('bomb30.png')
        self.flagImg =loadImage('flag.png')
        self.crossImg =loadImage('cross.png')
        
    def reveal(self):
        if not self.flagged:
            self.revealed = True
            if self.count == 0:
                self.flood = True

    
    def confirm(self):
        if self.x < mouseX < self.x + self.l and self.y < mouseY < self.y + self.l:
            return True     
    
    def countBombs(self, grid, rows, cols):
        if self.mine:
            self.count = -1
            return
        total = 0
        for xoff in range(-1, 2):
            cellX = self.row + xoff
            if cellX < 0 or cellX >= rows:
                continue
            for yoff in range(-1, 2):
                cellY = self.col + yoff
                if cellY < 0 or cellY >= cols:
                    continue
                neighbour = grid[cellX][cellY]
                if neighbour.mine:
                    total += 1
        self.count = total
    
    def floodFill(self, grid, rows, cols):
        for xoff in range(-1, 2):
            cellX = self.row + xoff
            if cellX < 0 or cellX >= rows:
                continue
            for yoff in range(-1, 2):
                cellY = self.col + yoff
                if cellY < 0 or cellY >= cols:
                    continue
                neighbour = grid[cellX][cellY]
                if (not neighbour.mine) and (not neighbour.revealed) and (not neighbour.flagged):
                    neighbour.reveal()
    
    def flag(self):
        self.flagged = True
    
    def unflag(self):
        self.flagged = False
    
    def show(self):
        stroke(0)
        strokeWeight(2)
        fill('#D9B3DF')
        rect(self.x, self.y, self.l, self.l)
        
        
        
        
        if self.revealed:              # Draws bombs
            if self.mine:
                fill('#4C0E56')
                rect(self.x, self.y, self.l, self.l)
                imageMode(CENTER)
                image(self.mineImg, self.x + self.l * 0.5, self.y + self.l * 0.5)
            else:
                fill(200)
                rect(self.x, self.y, self.l, self.l)
                
                textAlign(CENTER, CENTER)                #Texts
                textSize(self.l * 0.67)
                fill('#004D42')
                if not self.count == 0:
                    text(self.count, self.x + self.l * 0.5, self.y + self.l * 0.5)
        if self.flagged:
            imageMode(CENTER)
            image(self.flagImg, self.x + self.l * 0.5, self.y + self.l * 0.5)
            if self.wrongOne:
                image(self.crossImg, self.x + self.l * 0.5, self.y + self.l * 0.5)
            
                
