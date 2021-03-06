# Loop, play sound, do nothing
# mweldan@gmail.com, 2013
####################################
import pygame
import pygame.mixer
import os
import time
import sys
# constants like QUIT, KEYDOWN etc
from pygame.locals import * 

# set screen center on load
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
pygame.init() 

# set screen size to match picture
window = pygame.display.set_mode((468, 50)) 
pygame.display.set_caption('My first Pygame program') 
screen = pygame.display.get_surface() 
# fill screen with white color
screen.fill((255,255,255))
pic = os.path.join(".","nyan_cat_icon__3_by_kooliodragon-d3f22qi.gif")
surface = pygame.image.load(pic) 

sound = pygame.mixer.music
sound.load("nyan_cat.mp3")
sound.play(-1) 

x = 0
y = 0                 
 
while True:  
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            # use sys.exit() to quit
            sys.exit(1)
        elif event.type == KEYDOWN:
            if event.key == 27: # user press esc button
                sys.exit(1)
   
    screen.blit(surface, (x,y))     
    pygame.display.flip() 
    x += 1
    if x == 468:
        x = 0
    time.sleep(0.2)
                      
