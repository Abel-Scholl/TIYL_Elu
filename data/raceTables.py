from data.Table import Table
from data.races import races

class RaceTable(Table):
    def __init__(self):
        super().__init__()
        self.name = "Race"
        self.die = "1d100"
        self.options = []
        self.initializeOptions()
    
    def initializeOptions(self):
        for race in races:
            self.options.append({"name": race, "probability": races[race]["probability"]})
            
    def getOptionsList(self):
        return list(races.keys())
        


class HumanTable(Table):
    def __init__(self):
        super().__init__()
        self.name = "Human"
        self.die = "1d100"
        self.options = []
        self.initializeOptions()
    
    def initializeOptions(self):
        if races["Human"]["subtypes"]:
            subtypes = races["Human"]["subtypes"][0]
            for subtype in subtypes:
                self.options.append({"name": subtype, "probability": subtypes[subtype]["probability"]})
    
    def getOptionsList(self):
        return list(races["Human"]["subtypes"][0].keys())
        