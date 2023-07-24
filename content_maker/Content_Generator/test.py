import PIL
from PIL import Image, ImageDraw, ImageFont
import random
import PIL.ImageOps

#A4_DIMS = (2480, 3508)
A4_DIMS = (2400, 3400)
#A4_DIMS = (2174, 3075)
texts = [u"КА", u"КО", u"ЖУ"]

def outline_text(dr, pos, text, fnt, stroke, fill, stroke_width=6):
    "Draw outline-style text"
    dr.text((pos[0] - 1, pos[1]), text, font=fnt, fill=stroke, stroke_width=stroke_width)
    dr.text((pos[0] + 1, pos[1]), text, font=fnt, fill=stroke, stroke_width=stroke_width)
    dr.text((pos[0], pos[1] - 1), text, font=fnt, fill=stroke, stroke_width=stroke_width)
    dr.text((pos[0], pos[1] + 1), text, font=fnt, fill=stroke, stroke_width=stroke_width)
    dr.text(tuple(pos), text, font=fnt, fill=fill)

    #draw.text(digit_offset, ch, fill='white', font=font, stroke_width=2, stroke_fill='black')

def draw_coloring(texts):
    YC_WIDTH = A4_DIMS[0]
    YC_HEIGHT = A4_DIMS[1]
    FRAME_WIDTH = 200
    YC_BACKCOLOR = (255, 255, 255, 255)
    YC_BACKCOLOR_TR = (255, 255, 255, 0)
    YC_TEXTCOLOR = (0, 0, 0, 255)
    ROW_HEIGHT = 450
    WAVE_LENGTH = 100
    BOTTOM_PLACE = 400

    img = Image.new('RGBA', (YC_WIDTH, YC_HEIGHT), color=YC_BACKCOLOR)

    digit_sz = [0, 0]
    digit_offset = [FRAME_WIDTH, FRAME_WIDTH]
    row = 0
    b = False
    while True:
        while True:
            digit = random.choice(texts)
            font = ImageFont.truetype("Roboto-Regular.ttf", size=random.randint(100, 400), encoding="utf-8")
            txt = Image.new('RGBA', img.size, YC_BACKCOLOR_TR)
            draw = ImageDraw.Draw(txt)
            new_box = draw.textbbox((0, 0), digit, font)
            w = new_box[2] - new_box[0]  # bottom-top
            h = new_box[3] - new_box[1]  # right-left
            digit_sz = w, h
            digit_offset[0] += random.randint(0, WAVE_LENGTH)
            digit_offset[1] = FRAME_WIDTH + ROW_HEIGHT * row + random.randint(0, WAVE_LENGTH)

            if digit_offset[0] + w > YC_WIDTH - FRAME_WIDTH:
                break
            if digit_offset[1] + h > YC_HEIGHT - FRAME_WIDTH - BOTTOM_PLACE:
                b = True
                break
            print(digit_offset)
            #draw.line([(digit_offset[0] - 20, digit_offset[1] - 20), (digit_offset[0], digit_offset[1])],
            #          fill='blue', width=2, joint='curve')  # Horizontal
            outline_text(draw, digit_offset, digit, font, YC_TEXTCOLOR, YC_BACKCOLOR_TR)
            digit_offset[0] += digit_sz[0]

            img = Image.alpha_composite(img, txt)
            #img.show()
        if b:
            break
        digit_offset[0] = FRAME_WIDTH + random.randint(0, int(WAVE_LENGTH / 5))
        row += 1
        print(row)

    return img

def draw_hero(xy, img, hero):
    hero = hero.convert('L')
    hero = hero.point(lambda p: 255 if p > 200 else 0)
    mask = PIL.ImageOps.invert(hero)
    img.paste(hero, xy, mask)
    return img

if __name__ == "__main__":
    im = draw_coloring(texts)
    hero = Image.open('baby_shark.png')
    YC_WIDTH = A4_DIMS[0]
    YC_HEIGHT = A4_DIMS[1]
    xy = (YC_WIDTH - hero.size[0] - 50, YC_HEIGHT - hero.size[1] - 50)
    im = draw_hero(xy, im, hero)
    im.show()
    im.save("res.png")
