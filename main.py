from PIL import Image, ImageFont, ImageDraw
import os

image = Image.open("InputImage.png")
createImg = ImageDraw.Draw(image)

print("Image size:", image.size)

rochesterFontFolder = "rochester"
calligraphyFontFolder = "Antonellie-Calligraphy-Font"
rochesterFont = os.path.join(rochesterFontFolder, "Rochester-Regular.ttf")
calligraphyFont = os.path.join(calligraphyFontFolder, "Morning-Dew.otf")

mainFont = ImageFont.truetype(rochesterFont, 70)
secondaryFont = ImageFont.truetype(calligraphyFont, 35)
tertiaryFont = ImageFont.truetype(calligraphyFont, 30)
createFont = ImageFont.truetype(rochesterFont, 20)

mainText = "       Happy \n  Teacher's Day"
secondaryText = "Thank you for imparting your knowledge unto us."
tertiaryText = "   We will always be grateful \nto you for your support and kindness."
createText = "Created by - \nKanishaka Pranjal \nS20210010108"

createImg.text((90, 308), mainText, font=mainFont, fill="#6f694f")
createImg.text((60, 250), secondaryText, font=secondaryFont, fill="#ee9358")
createImg.text((120, 510), tertiaryText, font=tertiaryFont, fill="#ee9358")
createImg.text((400, 630), createText, font=createFont, fill="#f34f58")

image.save("OutputImage.png")

image.show()
