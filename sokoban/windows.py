import pygame

class sokoban_windows(object):
    def __init__(self, size, caption):
        self.size = size
        self.caption = caption
        
    def create(self):
        window = pygame.display
        screen = window.set_mode(self.size, 0, 24)
        window.get_surface().fill((255, 255, 255))
        
        # test show text 
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Hello World", True, (0, 0, 0), (255, 255, 255))
        screen.blit(text, (300, 250))
        
        window.set_caption(self.caption) 
        window.update()
