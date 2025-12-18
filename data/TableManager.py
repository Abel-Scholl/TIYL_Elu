import data.raceTables as raceTables

class TableManager:
    def __init__(self):
        self.tables = []
        self.addTable(raceTables.RaceTable())
        self.addTable(raceTables.HumanTable())

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
    
    def getTableList(self, table):
        t = self.getTableByName(table)
        result = t.getOptionsList()
        return result
        