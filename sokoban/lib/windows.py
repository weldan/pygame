"""
windows
"""

import pygame
import grid
import os
import settings

class sokoban_windows(object):
    def __init__(self):
        self.grid_setting = settings.grid_setting
        self.setting = settings.window_setting
        self.size = (self.setting['width'], self.setting['height'])
        self.caption = self.setting['title']
        self.window = pygame.display
        self.window.set_caption(self.caption)         
        self.screen = self.window.set_mode(self.size, 0, 24)
        self.grids = grid.sokoban_grid()
        self.grids.draw()
        pygame.display.flip()        

