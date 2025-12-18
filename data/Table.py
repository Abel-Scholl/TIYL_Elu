from abc import ABC, abstractmethod
import random

class Table(ABC):
    def __init__(self):
        self.name = ""
        self.items = []
        self.die = "" ##format: "1d6" number d number of sides (1-3 digits)
        self.modifier = 0
        self.options = []
        self.parentTable = None
        self.dependencies = [] ##tables that this table is dependent on
        self.supplementals = [] ##tables that are supplemental to this table (to add more flavor)
        ##when you add a supplemental table, it should push to the stack to be rolled on
    
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
            for subtype in self.options:
                cumulative += subtype["probability"] * 100
                if roll < cumulative:
                    return subtype["name"]
            return self.options[-1]["name"]
        else:
            return None
         
    
    def getItems(self):
        return self.items
    
    def getName(self):
        return self.name
    
    def getDie(self):
        return self.die
    
    def getModifier(self):
        return self.modifier