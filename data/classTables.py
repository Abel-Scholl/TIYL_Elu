from data.Table import Table
from data.classes import classes

class ClassTable(Table):
    def __init__(self, name="Class", die="1d100", depth=1):
        super().__init__()
        self.name = name
        self.die = die
        self.depth = depth
        
    def initializeOptions(self):
        if self.name == "Class":
            for class_ in classes:
                self.options.append({"name": class_, "probability": classes[class_]["probability"]})
        else:
            if classes[self.name]["subclasses"]:
                subclasses = classes[self.name]["subclasses"][0]
                for subclass in subclasses:
                    self.options.append({"name": subclass, "probability": subclasses[subclass]["probability"]})
    
    def getOptionsList(self):
        if self.name == "Class":
            return list(classes.keys())
        else:
            classOptions = classes[self.name]["subclasses"]
            if len(classOptions) > 0:
                return list(classOptions[0])
            else:
                return []
                
class SubclassTable()