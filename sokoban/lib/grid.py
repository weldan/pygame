"""
grids
"""

import pygame
import settings

class sokoban_grid(object):
    def __init__(self):
        self.setting = settings.grid_setting 
        self.size = (settings.window_setting['width'], settings.window_setting['height'])
        self.screen = pygame.display.set_mode(self.size, 0, 24)
    
    """
    draw grid
    """    
    def draw(self):
        pygame.display.get_surface().fill(self.setting['backgroundcolour'])
        self.grid = []
        for row in range(self.setting['rowsize']):
            self.grid.append([])
            for column in range(self.setting['columnsize']):
                self.grid[row].append(0)
                pygame.draw.rect(self.screen, 
                    self.setting['colour'], 
                    [
                        (self.setting['margin'] + self.setting['width']) 
                        * column 
                        + self.setting['margin'],
                        (self.setting['margin'] + self.setting['height']) 
                        * row 
                        + self.setting['margin'],
                        self.setting['width'],
                        self.setting['height']
                    ]
               )
        pygame.display.flip() 
    
    """
    get grid by row and column position
    """    
    def get(self, row, column):
        try:
            return self.grid[row][column]
        except IndexError:
            return 0
                             
        
                                       
