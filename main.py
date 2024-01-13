import math
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BACKGROUND_FILE = "background.jpg"
FONT_FILE = "UnicaOne-Regular.ttf"
NAMES_FILE = "names.txt"

pdfmetrics.registerFont(TTFont("custom_font", FONT_FILE))

canvas = Canvas("badge.pdf")
W, H = canvas._pagesize
diffs = [(0, 0), (0, 1), (1, 0), (1, 1)]
Names = []

with open(NAMES_FILE, "r") as f:
    lines = f.readlines()
    for line in lines:
        Names.append(line)

for i in range(math.ceil(len(Names) / 4)):

    for j, (dx, dy) in enumerate(diffs):
        if (4 * i + j) == len(Names):
            break

        x = W / 4 * (2 * dx + 1)
        y = H / 4 * (2 * dy + 1)
        name = Names[4 * i + j]
        title = " ".join(name.split(" ")[2:])
        name = " ".join(name.split(" ")[:2])

        canvas.drawImage(BACKGROUND_FILE, dx * W / 2, dy * H / 2, W / 2, H / 2)


        canvas.setFillColorRGB(1, 1, 1) # The text color - modify if needed

        canvas.setFont("custom_font", 32)
        canvas.drawCentredString(x, y - 16, name)
        canvas.setFont("custom_font", 14)
        canvas.drawCentredString(x, y + 20, title)

    canvas.line(W / 2, 0, W / 2, H)
    canvas.line(0, H / 2, W, H / 2)
    canvas.showPage()


canvas.save()
