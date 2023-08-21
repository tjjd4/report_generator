from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

w, h = A4

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

c = canvas.Canvas("hello-world.pdf", pagesize=A4)
c.setFont('STSong-Light', 16)

c.drawString(50, h - 50, "你好")
c.showPage()
c.save()