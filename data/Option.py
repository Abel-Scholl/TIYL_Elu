class Option:
    def __init__(self, name, probability=None):
        self.name = name
        self.probability = probability
        self.suppTables = []
    
    def getName(self):
        return self.name
    
    def getProbability(self):
        return self.probability
    
    def setProbability(self, probability):
        self.probability = probability
    
    def getSuppTables(self):
        return self.suppTables
    
    def addSuppTable(self, table):
        self.suppTables.append(table)
    
    def removeSuppTable(self, table):
        self.suppTables.remove(table)
    