# My first pygame (?)
# Move picture forward and backward on key press 
# mweldan@gmail.com, 2013
####################################
import pygame
import pygame.mixer
import os
# constants like QUIT, KEYDOWN etc
from pygame.locals import * 
 
pygame.init() 
 
window = pygame.display.set_mode((468, 60)) 
pygame.display.set_caption('My first Pygame program') 
screen = pygame.display.get_surface() 
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
            pygame.display.quit()
        elif event.type == KEYDOWN:
            if event.key == 27: # user press esc button
                pygame.display.quit()
            elif event.key == 275: # user press right arrow
                x += 1
                pygame.display.set_caption('Move forward!')
            elif event.key == 276: # user press left arrow 
                x -= 1
                pygame.display.set_caption('Move backward!')
            else: 
                pygame.display.set_caption('Run! Run! Run!')
   
    screen.blit(surface, (x,y))     
    pygame.display.flip()               
