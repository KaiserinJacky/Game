# currently a hodgepodge between me messing around with pygame and me messing around with stuff for the actual game
import pygame # pygame library
from enum import Enum

class Area(Enum): # idk how different enums in python are from enums in c++, so idk if this is the best option for menus and such
    MENU = 1
    MAP = 2
    COMBAT = 3

current_area = Area.MENU

# pygame stuff
pygame.init()
Screenwidth = 800
Screenheight = 600
scalex = Screenwidth / 100 # scale factors so that screen items aren't defined in pixel sizes
scaley = Screenheight / 100
# create screen
screen = pygame.display.set_mode((Screenwidth, Screenheight))

game = True # bool that controls game
while game: # main game loop

    if current_area == Area.MENU: # menu
        screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hit x button
            game = False

    pygame.display.update()

pygame.quit() # close window when game over