class Character:
    def __init__(self):
        self.name = None
        self.race = None
        self.racial_subtype = None
        self.class_ = None ##string, has a _ to differentiate from the keyword
        self.subclass = None ##string
        self.class_reason = None ##string
        self.level = 1
        self.background = None ##string
        self.background_reason = None ##string
        self.alignment = None ##string
        self.experience = 0
        self.proficiency_bonus = 0
        self.inspiration = 0
        self.hp = None
        self.armor_class = None
        self.initiative = 0
        self.walking_speed = None
        self.flying_speed = None
        self.swimming_speed = None
        self.climbing_speed = None
        
        
    def set(self, title, value):
        match title:
            case "Character Name":
                self.name = value
            case "Race":
                self.race = value
            case "Racial Subtype":
                self.racial_subtype = value
            case "Class":
                self.class_ = value
            case "Subclass":
                self.subclass = value
            case "Class Reason":
                self.class_reason = value
            case "Background":
                self.background = value
            case "Background Reason":
                self.background_reason = value
            case "Alignment":
                self.alignment = value
            case "Level":
                self.level = value
                
    def get(self, title):
        match title:
            case "Character Name":
                return self.name
            case "Race":
                return self.race
            case "Racial Subtype":
                return self.racial_subtype
            case "Class":
                return self.class_
            case "Subclass":
                return self.subclass
            case "Class Reason":
                return self.class_reason
            case "Background":
                return self.background
            case "Background Reason":
                return self.background_reason
            case "Alignment":
                return self.alignment
            case "Level":
                return self.level
            
            
    def getAll(self):
        return {
            "Character Name": self.name,
            "Level": self.level,
            "Race": self.race,
            "Racial Subtype": self.racial_subtype,
            "Class": self.class_,
            "Subclass": self.subclass,
            "Class Reason": self.class_reason,
            "Background": self.background,
            "Background Reason": self.background_reason,
            "Alignment": self.alignment,
            "Experience": self.experience,
            "Proficiency Bonus": self.proficiency_bonus,
            "Inspiration": self.inspiration,
            "HP": self.hp,
            "Armor Class": self.armor_class,
            "Initiative": self.initiative,
            "Walking Speed": self.walking_speed,
            "Flying Speed": self.flying_speed,
            "Swimming Speed": self.swimming_speed,
            "Climbing Speed": self.climbing_speed,
        }
                
        