import pygame
import sys

from pygame.locals import * 

class sokoban_events(object):
    def __init__(self):
        pass
        
    """
    listen events
    """
    def listen(self):
        events = pygame.event
        for self.event in events.get():
            if self.event.type == QUIT:
                sys.exit(1)
            elif self.event.type == KEYDOWN:
                if self.event.key == 27:
                    sys.exit(1)
            else:
                self.process() 

    """
    process event
    """
    def process(self):
        pass
        #print self.event              
