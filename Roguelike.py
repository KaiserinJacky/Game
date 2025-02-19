import dice
import pygame

# roguelike stuff

class Room: # room class
    def __init__(self, monsters, loot):
        self.monsters = monsters
        self.loot = loot
        # whatever else is needed for a room; map coords, what rooms it connects to, etc.
        # not sure yet what we'll need, exactly

current_room = Room("No Monsters", "No Loot") # initial empty room

class Creature: # Monsters and Players (And NPCs ??? - Later)
    def __init__(self, str, dex, int, speed, level, gear):
        self.str = str # strength
        self.dex = dex # dexterity
        self.int = int # intelligence
        self.speed = speed
        self.level = level
        self.maxhp = (str + 1) * level # maximum hit points
        self.hp = (str + 1) * level # current hit points - starts at max
        self.fc = 10 + str + level # fortitude class
        self.watk = str + level # weapon attack bonus
        self.melee_wdmg = str # weapon damage bonus
        self.maxsp = (dex + 1) * level # maximum stamina points
        self.sp = (dex + 1) * level # current stamina points - starts at max
        self.rc = 10 + dex + level # reflex class
        self.dex_watk = dex + level # weapon attack bonus for ranged and finesse weapons
        self.maxmp = (int + 1) * level # maximum mana points
        self.mp = (int + 1) * level # current mana points - starts at max
        self.wc = 10 + int + level # will class
        self.satk = int + level # spell attack bonus
        self.gear = gear # list of gear held

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
        # no extra attributes yet

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