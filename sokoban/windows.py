import pygame
import sys

class sokoban_windows(object):
    def __init__(self, size, caption):
        self.size = size
        self.caption = caption
        
    def create(self):
        window = pygame.display
        window.set_mode(self.size)
        window.set_caption(self.caption) 
        window.update()
