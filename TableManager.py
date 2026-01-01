from objects.Table import Table
from data.races import races
from data.classes import classes
from objects.Option import Option
from data.backgrounds import backgrounds
from data.parents import parents

class TableManager:
    def __init__(self):
        self.tables = []
        
        self.initializeTable("Race")
        self.initializeTable("Class")
        self.initializeTable("Background")
        self.initializeTable("Parents")
        

    def addTable(self, table):
        self.tables.append(table)
    
    def getTableByName(self, name):
        for table in self.tables:
            if table.getName() == name:
                return table
        return None
    
    def rollOnTableByName(self, name):
        table = self.getTableByName(name)
        if table is not None:
            return table.roll()
        return None
    
    def rollOnTable(self, table):
        if table is not None:
            return table.roll()
        return None
    
    def getTableOptionsNames(self, table):
        t = self.getTableByName(table)
        result = []
        if t is not None:
            for option in t.options:
                result.append(option.getName())
        return result
    
    def getAllTableNames(self):
        result = []
        for table in self.tables:
            result.append(table.name)
        return result
    
    def getTableOptionByName(self, name, table=None):
        if table is not None:
            for option in table.options:
                if option.getName() == name:
                    return option
        else:
            for t in self.tables:
                for option in t.options:
                    if option.getName() == name:
                        return option
        return None
    
    def initializeTable(self, tableType, name=None, parentType=None):
        ##based on the tableType, create a table with the appropriate options. 
        ##each option might have supplemental tables! This can help us handle that recursively.
        if name is None:
            name = tableType
        die = None
        options = []
        match tableType:
            case "Race":
                die = "1d100"
                ##get the list of races from the races dictionary
                for race in races:
                    option = Option(race, tableType, races[race]["probability"])
                    if races[race]["subtypes"]: ##If this has subtypes, a table needs to be created to roll for them
                        subTable =self.initializeTable("Racial Subtype", race)
                        ##add it to the option
                        option.addSuppTable(subTable)
                    options.append(option)
            
            case "Racial Subtype":
                die = "1d100"
                for subtype in races[name]["subtypes"][0]:
                    option = Option(subtype, tableType, races[name]["subtypes"][0][subtype]["probability"])
                    options.append(option)
                name = f"{name} Subtype"
                
            case "Class":
                die = "1d100"
                options = []
                probability = 1 / len(classes)
                ##get the list of classes from the classes dictionary
                for class_ in classes:
                    option = Option(class_, tableType, probability)
                    if classes[class_]["subclasses"]:
                        subTable = self.initializeTable("Subclass", class_)
                        option.addSuppTable(subTable)
                    #if classes[class_]["reasons"]:
                    #    subTable = self.initializeTable("Class Reason", class_)
                    #    option.addSuppTable(subTable)
                    options.append(option)

            case "Subclass":
                die = "1d100"
                probability = (1 / len(classes[name]["subclasses"]))
                for subclass in classes[name]["subclasses"]:
                    option = Option(subclass, tableType, probability)
                    options.append(option)
                name = classes[name]["subname"]
                    
            case "Class Reason":
                die = "1d100"
                probability = (1 / len(classes[name]["reasons"]))
                for reason in classes[name]["reasons"]:
                    option = Option(reason, tableType, probability)
                    options.append(option)
                name = f"{name} Class Reason"
            
            case "Background":
                die = "1d100"
                probability = (1 / len(backgrounds))
                for background in backgrounds:
                    option = Option(background, tableType, probability, backgrounds[background]["description"])
                    options.append(option)
            
            case "Parents":
                die = "1d100"
                for option in parents["options"]:
                    option = Option(option["name"], tableType, option["probability"])
                    options.append(option)
                name = "Parents"
                
            case _:
                return None
        
        table = Table(name=name, die=die, options=options)
        self.addTable(table)
        return table