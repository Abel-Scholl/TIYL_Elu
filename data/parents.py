parents = {
    "options": [
        {"name": "You know who your parents are", "probability": .95},
        {"name": "You don't know who your parents are", "probability": .05}
    ],
    "half-race options": [
        {
            "name": "half-elf", 
            "options": [
                {"option": ("Human", "Elf"), "description": "", "probability": .63},
                {"option": ("Elf", "Half-Elf"), "description": "", "probability": .12},
                {"option": ("Human", "Half-Elf"), "description": "", "probability": .13},
                {"option": ("Half-Elf", "Half-Elf"), "description": "", "probability": .12}
            ]
        }, 
        {
            "name": "half-orc",
            "options": [
                {"option": ("Human", "Orc"), "description": "", "probability": .4},
                {"option": ("Orc", "Half-Orc"), "description": "", "probability": .25},
                {"option": ("Human", "Half-Orc"), "description": "", "probability": .25},
                {"option": ("Half-Orc", "Half-Orc"), "description": "", "probability": .1}
            ]
        },
        {
            "name": "tiefling",
            "options": [
                {"option": ("Human", "Tiefling"), "description": "Your internal heritage was dormant until you came along.", "probability": .5},
                {"option": ("Human", "Human"), "description": "", "probability": .26},
                {"option": ("Tiefling", "Devil"), "description": "", "probability": .12},
                {"option": ("Human", "Devil"), "description": "", "probability": .12}
            ]
        }
    ]
}