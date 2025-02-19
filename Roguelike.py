import dice
import pygame

class Room: # room class
    def __init__(self, monsters, loot):
        self.monsters = monsters
        self.loot = loot
        # whatever else is needed for a room; map coords, what rooms it connects to, etc.
        # not sure yet what we'll need, exactly

current_room = Room("No Monsters", "No Loot") # initial empty room

    # gear + gear subclasses

class Gear: # gear class
    def __init__(self, kind):
        self.kind = kind # type of gear - weapon, armor, focus, etc

class Weapon(Gear):
    def __init__(self, damage_die, potency, traits):
        super().__init__("Weapon")
        self.damage_die = damage_die
        self.potency = potency
        self.traits = traits

class Armor(Gear):
    def __init__(self, ac_bonus, potency, traits):
        super().__init__("Armor")
        self.ac_bonus = ac_bonus
        self.potency = potency
        self.traits = traits

class Focus(Gear):
    def __init__(self, spells, potency, traits):
        super().__init__("Focus")
        self.spells = spells
        self.potency = potency
        self.traits = traits



class Artifact: # artifact class
    def __init__(self):
        # not sure what to put here yet. the artifacts are just a scrambled collection of special gear.
        # maybe shouldn't be its own class
        pass

class Spell: # spell class
    def __init__(self, defense, damage, mana_cost, partial, full, bonus):
        self.defense = defense # defense the spell targets
        self.damage = damage # damage the spell does
        self.mana_cost = mana_cost # mana cost of the spell
        self.partial = partial # partial effect of spell
        self.full = full # full effect of spell
        self.bonus = bonus # bonus effect of spell on a critical

    # creature and creature subclasses

class Creature: # Monsters and Players (And NPCs ??? - Later)
    def __init__(self, str, dex, int, per_base, speed, level, gear):
        self.str = str # strength
        self.dex = dex # dexterity
        self.int = int # intelligence
        self.per = per_base + level # perception
        self.speed = speed
        self.level = level
        self.ac = 10 # add armor bonus based on gear?
        self.maxhp = 8 + str * level # maximum hit points
        self.hp = 8 + str * level # current hit points - starts at max
        self.fc = 10 + str + level # fortitude class
        self.watk = str + level # weapon attack bonus
        self.melee_wdmg = str # weapon damage bonus
        self.maxsp = 8 + dex * level # maximum stamina points
        self.sp = 8 + dex * level # current stamina points - starts at max
        self.rc = 10 + dex + level # reflex class
        self.dex_watk = dex + level # weapon attack bonus for ranged and finesse weapons
        self.maxmp = 8 + int * level # maximum mana points
        self.mp = 8 + int * level # current mana points - starts at max
        self.wc = 10 + int + level # will class
        self.satk = int + level # spell attack bonus
        self.gear = gear # list of gear held

    def __str__(self):
        return f"Str: {self.str} - Dex: {self.dex} - Int: {self.int}\nLevel: {self.level} - Per: {self.per} - Spd: {self.speed}\nHP: {self.hp} - SP: {self.sp} - MP: {self.mp}"

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
    def __init__(self, str, dex, int, per_base, speed, level, gear):
        super().__init__(str, dex, int, per_base, speed, level, gear)
        # no extra attributes yet

    def die(self):
        for i in self.gear:
            current_room.loot.append(i) # drop gear into room


class Player(Creature): # class for player character - subclass of Creature
    def __init__(self, charclass, level):
        super().__init__(charclass.str_base, charclass.dex_base, charclass.int_base, charclass.per_base, charclass.speed_base, level, charclass.starting_gear)
        self.charclass = charclass

    def die(self):
        # "you lose" menu
        pass



class CharClass: # class for character classes
    def __init__(self, str_base, dex_base, int_base, per_base, speed_base, starting_gear):
        self.str_base = str_base # base strength
        self.dex_base = dex_base # base dexterity
        self.int_base = int_base # base intelligence
        self.per_base = per_base # base perception
        self.speed_base = speed_base # base speed
        self.starting_gear = starting_gear # starting gear for class

# define base classes
soldier = CharClass(3,1,1,2,20,("Basic Armor", "Basic Shield", "Basic Sword"))
sorcerer = CharClass(1,1,3,2,25, ("Basic Wand", "Wizard Robes"))
scoundrel = CharClass(1,3,1,3,30,"Basic Knife")

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