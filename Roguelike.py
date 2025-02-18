import dice
import pygame

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

class Creature2: # spitballing different creature definition
    def __init__(self, str, dex, int, speed, level):
        self.str = str
        self.dex = dex
        self.int = int
        self.speed = speed
        self.level = level
        self.maxhp = (str + 1) * level
        self.hp = (str + 1) * level
        self.fc = 10 + str + level
        self.watk = str + level
        self.melee_wdmg = str
        self.sp = (dex + 1) * level
        self.rc = 10 + dex + level
        self.dex_watk = dex + level
        self.mp = (int + 1) * level
        self.wc = 10 + int + level
        self.satk = int + level


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