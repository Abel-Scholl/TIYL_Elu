from PIL import Image, ImageTk


palette = {
    "background": "#757992", ##blue
    "heading": "#EE881A", ##orange/gold
    "color3": "#A41917", ##red
    "color4": "#819564", ##tan/green
    "color5": "#030F15", ##black
    "color6": "#F1DBB5", ##cream
    "color7": "#FAB65D" ##yellow/light gold
}

sections = {
    "Base": ["Character Name", "Level", "Race", "Background", "Class"],
    "Origins": ["Parents", "Birthplace", "Siblings", "Family", "Absent Parent", "Childhood Home", "Childhood Memories"],
    "Bonds": [], ##This is where people close to you will go. If you have family/siblings, the tables to roll on for them will show up here.
    "PersonalDecisions": ["Background", "Class"],
    "LifeEvents": ["Life Events"],
    "Supplemental": []
}

