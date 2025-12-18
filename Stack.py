class Stack:
    def __init__(self):
        self.items = [
            "Character Name", ##base
            "Race", ##base
            #"Background", ##base
            
            ##Origins
            #"Parents", ## has race dependencies
            #"Birthplace",
            #"Siblings", ## has supplemental tables
            
            #"Alignment", ##base
            "Class", ##base
        ]
        
        
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        return self.items.pop(0) ##remove and return the first item
    
    def peek(self):
        return self.items[0] ##return the first item
    
    def isEmpty(self):
        return len(self.items) == 0
    