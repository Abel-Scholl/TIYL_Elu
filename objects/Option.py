class Option:
    def __init__(self, name, parentTable, probability=None, description=""):
        self.name = name
        self.description = description
        self.probability = probability
        self.parentTable = parentTable
        self.suppTables = []
    
    def getName(self):
        return self.name
    
    def getProbability(self):
        return self.probability
    
    def setProbability(self, probability):
        self.probability = probability
        
    def getParentTable(self):
        return self.parentTable
    
    def getSuppTables(self):
        return self.suppTables
    
    def addSuppTable(self, table):
        self.suppTables.append(table)
    
    def removeSuppTable(self, table):
        self.suppTables.remove(table)
        
    def getDescription(self):
        return self.description
    