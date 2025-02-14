from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def coord(x, y, unit=1):
    x, y = x * unit, y * unit
    return x, y


c = canvas.Canvas("hello2.pdf", bottomup=0)

c.drawString(*coord(15, 20, mm), text="Welcome to Reportlab!")
c.showPage()
c.save()
