import csv

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

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

def getGroupRank(group_row):
    return scoresheet[group_row][FINAL_RANK_COL]

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

c = canvas.Canvas("hello-world.pdf", pagesize=A4)
c.setFont('STSong-Light', 16)

c.drawString(50, h - 50, "你好")
c.showPage()
c.save()