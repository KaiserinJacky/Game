# currently a hodgepodge between me messing around with pygame and me messing around with stuff for the actual game
import pygame # pygame library
import dice # dice library

# roguelike stuff
class Creature: # class for all creatures
    def __init__(self, hp, sp, mp, ac, rc, fc, wc, speed, gear):
        self.hp = hp # hit points
        self.sp = sp # stamina points
        self.mp = mp # mana points
        self.ac = ac # armor class
        self.rc = rc # reflex class
        self.fc = fc # fortitude class
        self.wc = wc # will class
        self.speed = speed # movement speed
        self.gear = gear # array of gear held by creature

class Player: # class for player character - subclass of Creature
    def __init__(self, hp, sp, mp, ac, rc, fc, wc, speed, gear, charclass):
        super().__init__(hp, sp, mp, ac, rc, fc, wc, speed, gear)
        self.charclass = charclass

def check(dc, bonus):
    roll = dice.roll('1d20') + bonus
    if roll < dc - 10:
        return "Failure" # no effect
    elif roll < dc:
        return "Partial" # half SP damage and partial effect
    elif roll >= dc and not roll >= dc + 10: # only if roll >= DC and not a critical
        return "Success" # full SP damage and full effect
    else: # roll >= dc + 10
        return "Critical" # full SP damage, full HP damage, full effect, and bonus effect

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hit x button
            game = False

    pygame.display.update()

pygame.quit()