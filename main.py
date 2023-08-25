import csv

from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

GROUP1_ROW = 2
GROUP2_ROW = 3
GROUP3_ROW = 4
GROUP4_ROW = 5
GROUP5_ROW = 6
GROUP6_ROW = 7
GROUP7_ROW = 8
GROUP8_ROW = 9

FINAL_RANK_COL = 14

w, h = A4
with open("./score_sheet - scoresheet1.csv", 'r', encoding="utf8", newline='') as file:
    csvreader = csv.reader(file)
    scoresheet = list(csvreader)

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

doc = SimpleDocTemplate('hello-world.pdf')

flowable = []

sample_style_sheet = getSampleStyleSheet()

def firstPageSetup(canvas, doc):
    canvas.saveState()
    canvas.drawImage('./report_template.png', 0, 0)
    canvas.restoreState()
bogustext = ("This is Paragraph number") *20
p = Paragraph(bogustext, sample_style_sheet['Normal'])
flowable.append(p)
doc.build(flowable, onFirstPage=firstPageSetup)