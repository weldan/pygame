import pygame

class sokoban_grid(object):
    def __init__(self, screen, width, height, margin, 
        colour, rowsize, columnsize, backgroundcolour):
        self.screen = screen
        self.width = width
        self.height = height
        self.margin = margin 
        self.colour = colour
        self.rowsize = rowsize
        self.columnsize = columnsize
        self.backgroundcolour = backgroundcolour
    
    """
    draw grid
    """    
    def draw(self):
        pygame.display.get_surface().fill(self.backgroundcolour)
        self.grid = []
        for row in range(self.rowsize):
            self.grid.append([])
            for column in range(self.columnsize):
                self.grid[row].append(0)
                pygame.draw.rect(self.screen, 
                    self.colour, 
                    [
                        (self.margin + self.width) 
                        * column 
                        + self.margin,
                        (self.margin + self.height) 
                        * row 
                        + self.margin,
                        self.width,
                        self.height
                    ]
               )
        pygame.display.flip() 
    
    """
    get grid by row and column position
    """    
    def get(self, row, column):
        return self.grid[row][column]
                        
