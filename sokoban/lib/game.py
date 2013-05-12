"""
game
"""

import pygame
import os 
import windows
import settings
import player
import events

def run():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    
    window = windows.sokoban_windows()   
    user = player.sokoban_player(window.grids.grid)
    
    while True:
        sokoban_events = events.sokoban_events(user)
        sokoban_events.listen()    
    
        #import ipdb
        #ipdb.set_trace()
