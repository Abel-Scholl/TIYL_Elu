from data.Table import Table
from data.races import races

class RaceTable(Table):
    def __init__(self, name="Race", die="1d100"):
        super().__init__()
        self.name = name
        self.die = die
        self.initializeOptions()
        
    def initializeOptions(self):
        if self.name == "Race":
            for race in races:
                self.options[0].append({"name": race, "probability": races[race]["probability"]})
        else:
            name = self.name.split(" ")[0] 
            ##and remove ' and - from the name
            name = name.replace("'", "").replace("-", "")
            
            if races[self.name]["subtypes"]:
                subtypes = races[self.name]["subtypes"][0]
                for subtype in subtypes:
                    self.options.append({"name": subtype, "probability": subtypes[subtype]["probability"]})
        
    def getOptionsList(self):
        if self.name == "Race":
            return list(races.keys())
        else:
            raceOptions = races[self.name]["subtypes"]
            if len(raceOptions) > 0:
                return list(raceOptions[0].keys())
            else:
                return []
