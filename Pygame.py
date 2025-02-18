# currently a hodgepodge between me messing around with pygame and me messing around with stuff for the actual game
import pygame # pygame library

# pygame stuff
pygame.init()
Screenwidth = 800
Screenheight = 600
# create screen
screen = pygame.display.set_mode((Screenwidth, Screenheight))

# dummy player
player = pygame.Rect((300,250,50,50))

game = True # bool that controls game
while game:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1,0)
    if key[pygame.K_d]:
        player.move_ip(1, 0)
    if key[pygame.K_s]:
        player.move_ip(0, 1)
    if key[pygame.K_w]:
        player.move_ip(0, -1)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hit x button
            game = False

    pygame.display.update()

pygame.quit()