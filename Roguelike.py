import dice
import pygame

# roguelike stuff

class Room: # room class
    def __init__(self, monsters, loot):
        self.monsters = monsters
        self.loot = loot

current_room = Room() # initial empty room

class Creature: # Monsters and Players (And NPCs ??? - Later)
    def __init__(self, str, dex, int, speed, level, gear):
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
        self.gear = gear

    def damage(self,damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()
    def heal(self,heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    def die(self):
        # different for subclasses
        raise NotImplementedError("Subclasses must implement this method")

class Monster(Creature): # class for monsters - subclass of Creature
    def __init__(self, str, dex, int, speed, level, gear):
        super().__init__(str, dex, int, speed, level, gear)

    def die(self):
        for i in self.gear:
            current_room.loot.append(i) # drop gear into room


class Player(Creature): # class for player character - subclass of Creature
    def __init__(self, str, dex, int, speed, level, charclass, gear):
        super().__init__(str, dex, int, speed, level, gear)
        self.charclass = charclass

    def die(self):
        # "you lose" menu
        pass

def check(bonus, dc):
    roll = dice.roll('1d20') + bonus
    if roll < dc - 10:
        return "Failure" # no effect
    elif roll < dc:
        return "Partial" # half SP damage and partial effect
    elif roll >= dc and not roll >= dc + 10: # only if roll >= DC and not a critical
        return "Success" # full SP damage and full effect
    else: # roll >= dc + 10
        return "Critical" # full SP damage, full HP damage, full effect, and bonus effect