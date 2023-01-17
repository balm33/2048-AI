###########
# Imports #
###########
import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

#############
# Variables #
#############
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

##################
# Initialization #
##################
winHeight = 600 
winWidth = 800
WINDOW = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)
# font = pygame.font.Font("PATHTOFONT", 20)
# pygame.display.set_caption("NAME")

###########
# Classes #
###########
class Player():
    def __init__(self):
        self.surf = pygame.surface.Surface((50, 50))
        self.rect = self.surf.get_rect(midbottom=(50, 50))
        self.surf.fill(WHITE)

    def event(self):
        pass

    def move(self):
        pass

    def draw(self):
        WINDOW.blit(self.surf, self.rect)

####################
# Class References #
####################
player = Player()

#############
# Game Loop #
#############
while True:
    # fill screen every frame
    WINDOW.fill(BLACK)

    for event in pygame.event.get():
        #quit fuctionality
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # escape key to quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    player.draw()
    pygame.display.update()