import data.raceTables as raceTables

class TableManager:
    def __init__(self):
        self.tables = []
        self.addTable(raceTables.RaceTable())
        self.addTable(raceTables.HumanTable())
        self.addTable(raceTables.DwarfTable())
        self.addTable(raceTables.ElfTable())
        self.addTable(raceTables.OrcTable())
        self.addTable(raceTables.HalflingTable())
        self.addTable(raceTables.GnomeTable())
        self.addTable(raceTables.DraconidTable())
        self.addTable(raceTables.HalfGiantTable())
        self.addTable(raceTables.GoblinoidTable())
        self.addTable(raceTables.CaznynTable())
        self.addTable(raceTables.MinotaurTable())
        self.addTable(raceTables.ThavlaniTable())
        self.addTable(raceTables.UurdakhTable())
        self.addTable(raceTables.XalnaarTable())
        self.addTable(raceTables.AulaiTable())
        self.addTable(raceTables.AutomatonTable())
        self.addTable(raceTables.SkjaltTable())
        self.addTable(raceTables.SkinchangerTable())
        self.addTable(raceTables.VanaraiTable())
        self.addTable(raceTables.DMChoiceTable())

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
    
    def getAllTableNames(self):
        result = []
        for table in self.tables:
            result.append(table.name)
        return result
        