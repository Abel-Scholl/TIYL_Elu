from data.Table import Table
from data.races import races

class RaceBaseTable(Table):
    def __init__(self):
        super().__init__()
        
    def initializeOptions(self):
        if self.name == "Race":
            for race in races:
                self.options.append({"name": race, "probability": races[race]["probability"]})
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


class RaceTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Race"
        self.die = "1d100"
        self.initializeOptions()
    
class HumanTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Human"
        self.die = "1d100"
        self.initializeOptions()
        
class DwarfTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Dwarf"
        self.die = "1d100"
        self.initializeOptions()
        
class ElfTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Elf"
        self.die = "1d100"
        self.initializeOptions()
        
class OrcTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.die = "1d100"
        self.initializeOptions()
        
class HalflingTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Halfling"
        self.die = "1d100"
        self.initializeOptions()
        
class GnomeTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Gnome"
        self.die = "1d100"
        self.initializeOptions()
        
class DraconidTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Draconid (Dragonborn)"
        self.die = "1d100"
        self.initializeOptions()
        
class HalfGiantTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Half-Giant (Goliath)"
        self.die = "1d100"
        self.initializeOptions()
        
class GoblinoidTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Goblinoid"
        self.die = "1d100"
        self.initializeOptions()
        
class IltheraiTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Iltherai (Kalashtar)"
        self.die = "1d100"
        self.initializeOptions()
        
class LizardfolkTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Lizardfolk"
        self.die = "1d100"
        self.initializeOptions()
        
class NaelingTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Naeling (Tiefling)"
        self.die = "1d100"
        self.initializeOptions()
        
class MarenatiTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Marenati (Triton)"
        self.die = "1d100"
        self.initializeOptions()
        
class CaznynTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Caznyn (Tabaxi / Leonin)"
        self.die = "1d100"
        self.initializeOptions()
        
class MinotaurTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Minotaur"
        self.die = "1d100"
        self.initializeOptions()
        
class ThavlaniTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Thavlani (Vedalken)"
        self.die = "1d100"
        self.initializeOptions()
        
class UurdakhTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Uurd'akh (Simic Hybrid)"
        self.die = "1d100"
        self.initializeOptions()
        
class XalnaarTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Xalnaar (Yuan-ti)"
        self.die = "1d100"
        self.initializeOptions()
        
class AulaiTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Aulai (Aasimar)"
        self.die = "1d100"
        self.initializeOptions()
        
class AutomatonTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Automaton (Warforged)"
        self.die = "1d100"
        self.initializeOptions()
        
class SkjaltTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Skjalt (Shifter)"
        self.die = "1d100"
        self.initializeOptions()
        
class SkinchangerTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Skinchanger (Changeling)"
        self.die = "1d100"
        
class VanaraiTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "Vanarai (Eladrin)"
        self.die = "1d100"
        self.initializeOptions()
        
class DMChoiceTable(RaceBaseTable):
    def __init__(self):
        super().__init__()
        self.name = "DM Choice"
        self.die = "1d100"
        self.initializeOptions()
        