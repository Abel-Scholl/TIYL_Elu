from abc import ABC, abstractmethod
import random

class Table(ABC):
    def __init__(self, name="", die="1d100", modifier=0, options=[], parentTable=None):
        self.name = name
        self.die = die
        self.modifier = modifier
        self.options = options
        self.parentTable = parentTable
    
    def addModifier(self, modifier):
        self.modifier = modifier
    
    def roll(self):
        d = self.die.split("d")
        limit = int(d[0]) * int(d[1]) ##number of dice rolled * number of sides
        roll = random.randint(int(d[0]), limit) + self.modifier
        result = self.handleRoll(roll - int(d[0])) ##subtract the number of dice rolled to get the actual roll. Ex: 2d6 roll of 5, 2 = 8 is actually 3 for table purposes.
        return result
    
    def handleRoll(self, roll):
        if self.options:
            cumulative = 0
            for option in self.options:
                cumulative += option.getProbability() * 100
                if roll < cumulative:
                    return option.getName()
            return self.options[-1].getName()
        else:
            return None
    
    def getName(self):
        return self.name
    
    def getDie(self):
        return self.die
    
    def getModifier(self):
        return self.modifier