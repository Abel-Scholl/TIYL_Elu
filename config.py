from PIL import Image, ImageTk

palette = {
    "color1": "#757992", ##blue
    "color2": "#EE881A", ##orange/gold
    "color3": "#A41917", ##red
    "color4": "#819564", ##tan/green
    "color5": "#030F15", ##black
    "color6": "#F1DBB5" ##cream
}
dice_image = Image.open("./assets/dice.png")
dice_image = dice_image.resize((dice_image.width // 4, dice_image.height // 4))
dice_images = {
    "d100": dice_image.crop((0, 0, 30, 40)),
    "d10": dice_image.crop((0, 0, 30, 40)),
    "d12": dice_image.crop((70, 0, 110, 40)),
    "d20": dice_image.crop((110, 0, 150, 40)),
    "d8": dice_image.crop((115, 0, 160, 40)),
    "d6": dice_image.crop((30, 0, 70, 40)),
    "d4": dice_image.crop((30, 0, 70, 40))
}

for key, value in dice_images.items():
    dice_images[key] = ImageTk.PhotoImage(value)