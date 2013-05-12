"""
events
"""

import pygame
import sys

from pygame.locals import * 

class sokoban_events(object):
    def __init__(self, player):
        self.player = player
        
    """
    listen events
    """
    def listen(self):
        events = pygame.event
        for self.event in events.get():
            if self.event.type == QUIT:
                sys.exit(1)
            elif self.event.type == KEYDOWN:
                if self.event.key == pygame.K_ESCAPE:
                    sys.exit(1)
                elif self.event.key == pygame.K_UP:
                    self.player.move_up()
                elif self.event.key == pygame.K_DOWN:
                    self.player.move_down()
                elif self.event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif self.event.key == pygame.K_LEFT:
                    self.player.move_left()    
            else:
                self.process() 

    """
    process event
    """
    def process(self):
        print self.event              
