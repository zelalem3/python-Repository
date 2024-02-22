from PIL import Image, ImageDraw, ImageFont
base = Image.open("Online-Learning-Social-1.jpg").convert("RGBA")
txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
font_size = 40
font = ImageFont.truetype("Roboto-Italic.ttf", font_size)
draw = ImageDraw.Draw(txt)
watermark_text = "The watermark has been added"
x = 40
y = 200
draw.text((x, y), watermark_text, font=font, fill=(255, 0, 0, 128))
out = Image.alpha_composite(base, txt)
out.show()
