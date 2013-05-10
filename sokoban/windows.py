import pygame
import grid
import os

class sokoban_windows(object):
    def __init__(self, size, caption):
        self.size = size
        self.caption = caption
        
    def create(self):    
        window = pygame.display
        window.set_caption(self.caption)         
        screen = window.set_mode(self.size, 0, 24)
        
        # to use with class grid
        width = 79
        height = 59
        margin = 1
        colour = (255, 255, 255)
        rowsize = 10
        columnsize = 10
        backgroundcolour = (0, 0, 0)
      
        grids = grid.sokoban_grid(
            screen, 
            width, 
            height, 
            margin, 
            colour,
            rowsize,
            columnsize,
            backgroundcolour
        )
        grids.draw()
        
        pic = os.path.join("data","stickmang.resized.jpg")
        gambo = pygame.image.load(pic)
        # stick man 
        grids.grid[0][0] = window.get_surface().blit(gambo, (10,10))
        window.update()         
