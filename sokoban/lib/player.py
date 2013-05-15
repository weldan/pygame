"""
player
"""

import pygame
import settings
import grid as grids

class sokoban_player(object):
    def __init__(self, grid):
        self.setting = settings.player_setting  
        self.grid_setting = settings.grid_setting
        self.grid = grid
        self.grid_on_screen = grids.sokoban_grid()
        self.window = pygame.display 
        self.draw()
                
    def draw(self):
        self.grid_on_screen.draw()
        player_image = pygame.image.load(self.setting['image'])
        try:
            width_position = self.grid_setting['width'] * self.location_column + 10
            height_position = self.grid_setting['height'] * self.location_row + 10
            self.grid[self.location_row][self.location_column] = self.window.get_surface().blit(
                player_image, (width_position, height_position)
            )                          
        except AttributeError:
            self.location_row = 0
            self.location_column = 0
            self.grid[self.location_row][self.location_column] = self.window.get_surface().blit(
                player_image, (10,10)
            )            
        pygame.display.flip()
        
    def clear(self):
        try:
            self.grid[self.location_row][self.location_column] = 0       
        except IndexError:
            return False
            
    def move_up(self):
        self.clear()
        self.location_row = self.location_row-1
        if self.location_row < 0:
            self.location_row = 0
        else:
            self.draw()    

    def move_down(self):
        self.clear()
        self.location_row = self.location_row+1
        if self.location_row > 9:
            self.location_row = 9
        else:
            self.draw()    

    def move_right(self):
        self.clear()
        self.location_column = self.location_column+1
        if self.location_column > 9:
            self.location_column = 9
        else:    
            self.draw()  
        
    def move_left(self):
        self.clear()
        self.location_column = self.location_column-1
        if self.location_column < 0:
            self.location_column = 0
        else:    
            self.draw()                   
