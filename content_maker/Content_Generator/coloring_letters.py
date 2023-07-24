from PIL import Image, ImageDraw, ImageFont
import os, glob
import numpy as np
import random

parentPath = "CaptchaDataset\\"

charactersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                  '8', '9']
fontTypes = []

for font in glob.glob("fonts\\*"):  # Create Image for every font
    fontTypes.append(os.path.abspath(font))

font = ImageFont.load_default()
fontTypes.append(font)

for index, character in enumerate(charactersList):
    path = os.path.join(parentPath, character + "_" + str(index))

    if not os.path.exists(path):
        os.mkdir(path)

    for imageCounter in range(len(fontTypes)):
        print(imageCounter)
        for repeats in range(3):  # Number of Images
            # img = Image.new('1', (28, 28), color = 'black')
            fnt = ImageFont.truetype(fontTypes[imageCounter], random.randint(30, 50))
            w, h = fnt.getsize(character)
            img_w, img_h = w + 20, h + 20  # Add 20 pixels padding (assume 10 pixels from each side).
            img = Image.new('L', (img_w, img_h),
                            color='black')  # Replace '1' with 'L' (8-bit pixels, black and white - we fill 255 so we can't use 1 bit per pixel)
            d = ImageDraw.Draw(img)
            d.text(((img_w - w) / 2, (img_h - h) / 2), character, font=fnt, fill=255,
                   align="center")  # TO ALIGN CHARACTER IN CENTER
            # img = np.pad(img, pad_width=10, mode='constant', constant_values=0) #Manually added padding
            # img = Image.fromarray(img)
            img.save(path + "\\" + str(imageCounter) + "_" + str(repeats) + ".jpg")
        break