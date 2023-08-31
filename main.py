import csv

from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, TableStyle, Table
from reportlab.platypus import Paragraph, Spacer, Image

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

GROUP_AMOUNT = 6

SCORESHEET_GROUP_START_ROW = 2

SCORESHEET_GAME1_RANK_COL = 2
SCORESHEET_GAME2_RANK_COL = 5
SCORESHEET_GAME3_RANK_COL = 8
SCORESHEET_GAME4_RANK_COL = 11
SCORESHEET_FINAL_RANK_COL = 14

GROUP_START_ROW = 0
GAME1_COL = 1
GAME2_COL = 2
GAME3_COL = 3
GAME4_COL = 4
FINAL_COL = 5
Q1_COL = 7
Q2_COL = 8
Q3_COL = 9
Q4_COL = 10
Q5_COL = 11
Q6_COL = 12
Q7_COL = 13
Q8_COL = 14

w, h = A4

groups_data = []

with open("./scoresheet1.csv", 'r', encoding="utf8", newline='') as file:
    csvreader = csv.reader(file)
    scoresheet = list(csvreader)
    group_num = 1
    for group in range(SCORESHEET_GROUP_START_ROW, SCORESHEET_GROUP_START_ROW + GROUP_AMOUNT):
        groups_data.append([group_num, 
                            int(scoresheet[group][SCORESHEET_GAME1_RANK_COL]), 
                            int(scoresheet[group][SCORESHEET_GAME2_RANK_COL]), 
                            int(scoresheet[group][SCORESHEET_GAME3_RANK_COL]), 
                            int(scoresheet[group][SCORESHEET_GAME4_RANK_COL]), 
                            int(scoresheet[group][SCORESHEET_FINAL_RANK_COL])])
        group_num += 1

with open("./questionnaire1.csv", 'r', encoding="utf8", newline='') as file:
    csvreader = csv.reader(file)
    questionnaire = list(csvreader)
    for row in questionnaire:
        match row[1]:
            case "第1組":
                groups_data[0].append(row[2])
                groups_data[0].extend(row[7:15])
            case "第2組":
                groups_data[1].append(row[2])
                groups_data[1].extend(row[7:15])
            case "第3組":
                groups_data[2].append(row[2])
                groups_data[2].extend(row[7:15])
            case "第4組":
                groups_data[3].append(row[2])
                groups_data[3].extend(row[7:15])
            case "第5組":
                groups_data[4].append(row[2])
                groups_data[4].extend(row[7:15])
            case "第6組":
                groups_data[5].append(row[2])
                groups_data[5].extend(row[7:15])
            case _:
                pass

pdfmetrics.registerFont(TTFont('kaiu', "font/kaiu.ttf"))
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

def getRank(group, game = FINAL_COL):
    if group >= 0 and group < GROUP_AMOUNT and game > 0 and game <= 5:
        return groups_data[group][game]
    else:
        raise Exception("Wrong group or game number")

def firstPageSetup(canvas, doc):
    canvas.saveState()
    canvas.drawImage('./images/report_template.png', 0, 0)
    canvas.drawImage(getRankIconPath(doc.group), 100, h-300, width=150, height=150, mask='auto')
    canvas.restoreState()

def getRankIconPath(group):
    if getRank(group) == 1:
        return './images/lion_icon.png'
    elif getRank(group, GAME1_COL) == 1:
        return './images/chicken_icon.png'
    elif getRank(group, GAME2_COL) == 1:
        return './images/tiger_icon.png'
    elif getRank(group, GAME3_COL) == 1:
        return './images/dolphin_icon.png'
    elif getRank(group, GAME4_COL) == 1:
        return './images/cat_icon.png'
    else:
        return './images/koala_icon.png'

sample_style_sheet = getSampleStyleSheet()

title1 = '<img src="./images/icon.png" valign="middle" width="20" height="20"/> 團體評評理'

def getText1(group):
    if getRank(group) == 1:
        return '恭喜玩家們在一連串的關卡中脫穎而出，在所有關卡中分數加總最高，<br/>是今天的佼佼者啊！森林之王頒給你們是實至名歸。'
    elif getRank(group, GAME1_COL) == 1:
        return '恭喜玩家們是今天所有組別中平衡感最好的玩家團隊，<br/>怎麼樣都不會倒捏！<br/>難不倒咕咕雞稱號非你們莫屬！相信生活中也事事難不倒你們！'
    elif getRank(group, GAME2_COL) == 1:
        return '恭喜玩家們是今天所有組別中最敏捷的玩家團隊，若你們說第二，<br/>沒有其他人敢稱第一啦！我們森林中的敏捷小老虎稱號非你們莫屬！'
    elif getRank(group, GAME3_COL) == 1:
        return '恭喜玩家們是今天所有組別中肌力最好的玩家團隊，是不是平常有在練！<br/>看見你們的肌力也激勵了我們，激勵人心小海豚 嗚呼～！'
    elif getRank(group, GAME4_COL) == 1:
        return '恭喜玩家們是今天所有組別中最軟Ｑ的玩家團隊，是不是平常有在練！<br/>柔情似水小貓咪這個稱號太適合你們啦！可活潑可俏皮～'
    else:    
        return '玩家們在所有關卡中的表現都很平均哦！穩穩地完成了每一項關卡，<br/>我們不跟別人比，保持自己的身體在良好的狀況是最重要的。'

title1StyleCustom = ParagraphStyle(
    'title1StyleCustom',
    fontName='kaiu',
    alignment = 0,
    leftIndent = 200,
    parent=sample_style_sheet["Title"],
)

text1StyleCustom = ParagraphStyle(
    'text2StyleCustom',
    fontName='kaiu',
    fontSize=13,
    alignment = 0,
    leading=16,
    leftIndent = 220,
    parent=sample_style_sheet["Normal"],
)

title2 = '<img src="./images/icon.png" valign="middle" width="20" height="20"/> 身體健康望周知'

def getText2(group):
    q = []
    perfect = True

    if groups_data[group][Q1_COL] == '是':
        q.append("認知功能")
        perfect = False
    if groups_data[group][Q2_COL] == '是':
        q.append("行動功能")
        perfect = False
    if groups_data[group][Q3_COL] == '是':
        q.append("營養不良")
        perfect = False
    if groups_data[group][Q4_COL] == '是':
        q.append("視力障礙")
        perfect = False
    if groups_data[group][Q5_COL] == '不可以':
        q.append("聽力障礙")
        perfect = False
    if groups_data[group][Q6_COL] == '是':
        q.append("憂鬱")
        perfect = False
    if groups_data[group][Q7_COL] == '是':
        q.append("用藥")
        perfect = False
    if groups_data[group][Q8_COL] == '是':
        q.append("生活目標")
        perfect = False
    
    if perfect:
        return "嘿～剛剛從回饋問卷中依照長者整合式評估的結果出爐！<br/>你們這組高年級玩家的身體狀態：非常健康，老當益壯！"
    else:
        problem = ""
        for str in q:
            if problem == "":
                problem = str
            else:
                problem = problem + '、' + str
        return f"您在 {problem} 方面有潛在的風險，建議您至家醫科或老年醫學科，進一步評估與追蹤"

title2StyleCustom = ParagraphStyle(
    'title2StyleCustom',
    fontName='kaiu',
    alignment = 0,
    parent=sample_style_sheet["Title"],
)

text2StyleCustom = ParagraphStyle(
    'text2StyleCustom',
    fontName='kaiu',
    fontSize=13,
    alignment = 0,
    leading=16,
    leftIndent = 20,
    spaceAfter=10,
    parent=sample_style_sheet["Normal"],
)

title3 = '<img src="./images/icon.png" valign="middle" width="20" height="20"/> 你的感受我在乎'

text3 = '今天的關卡設計中，我們其實有暗藏一些小巧思。<br/>第一是我們四個關卡分別以平衡、敏捷、肌力與柔軟四大面向來規劃！<br/>第二呢，那就是設計發想皆是來自於高齡者體適能檢測項目喔！<br/>希望你們在做些關卡的時候也對這些項目更有認識！'

table_data = [['關卡名稱', '檢測項目'],
              ['平衡超雞群', '30 秒單腳站立'],
              ['路很難走', '8 英呎起身繞行（2.44 公尺）'],
              ['站立起乩', '椅子坐立'],
              ['軟爛的人', '抓背測驗、椅子坐姿體前彎']]

tableStyle = TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # 置中對齊
    ('FONTNAME', (0, 0), (-1, -1), 'kaiu'), # 字體
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), # 上下置中
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.Color(1.00000,0.60000,0.60000)), # width 0.5
    ('BACKGROUND', (0, 0), (-1, 0), colors.Color(1.00000,0.80392,0.80392)),
])

text4 = '之後回去也不妨多練習這些動作來提升體適能唷！'

text4StyleCustom = ParagraphStyle(
    'text4StyleCustom',
    fontName='kaiu',
    fontSize=13,
    leading=16,
    leftIndent = 20,
    spaceBefore=10,
    parent=sample_style_sheet["Normal"],
)

def getText5(group):
    if group >= 0 and group < GROUP_AMOUNT:
        match groups_data[group][6]:
            case "我現在無法說話，或只能說一個字":
                return '而透過今天短短的相處，我們發現：<br/>今天的運動強度對你來說有點太吃力啦！<br/>建議可以參考衛福部的運動影片跟著動一動或是使用我們的每日任務提醒<br/>，我們將提供難度適中的任務，每日定期發送給您！<br/>相信只要持之以恆，天天動一動，體能會越來越好的！'
            case "只能說兩三個字，別再逼我......":
                return '今天的運動強度對你來說有點小吃力哦！<br/>建議可以參考衛福部的運動影片跟著動一動或是使用我們的每日任務提醒，我們將提供難度適中的任務，每日定期發送給您！<br/>相信只要持之以恆，天天動一動，體能會越來越好的！'
            case '是可以說話，但是要我唱歌...我做不到！！':
                return "今天的運動強度對你來說剛剛好捏！<br/>建議可以照著像今天這樣的運動強度，每天動一動哦！<br/>也可以使用我們的每日任務提醒，我們將提供難度適中的任務，每日定期發送給您！<br/>擁有健康的身體，才可以隨心所欲的生活！"
            case '欸～我還可以唱歌喔！':
                return "哇！今天的運動強度對你來說簡直是小菜一碟捏！<br/>看來有好好在保養身體，請要繼續維持哦！<br/><br/>Good health is always young."
            case _:
                raise Exception("Data Error")
    else:
        raise Exception("Wrong group or game number")

        
if __name__ == '__main__':
    for group in range(GROUP_AMOUNT):
        doc = SimpleDocTemplate(f'./build/第{group+1}組健康報告書.pdf')
        flowable = []

        doc.group = group

        s = Spacer(0, 120)
        flowable.append(s)

        p = Paragraph(title1, title1StyleCustom)
        flowable.append(p)

        p = Paragraph(getText1(group), text1StyleCustom)
        flowable.append(p)

        s = Spacer(0, 10)
        flowable.append(s)

        p = Paragraph(title2, title2StyleCustom)
        flowable.append(p)

        p = Paragraph(getText2(group), text2StyleCustom)
        flowable.append(p)

        p = Paragraph(title3, title2StyleCustom)
        flowable.append(p)

        p = Paragraph(text3, text2StyleCustom)
        flowable.append(p)

        table = Table(table_data, [150,250],35, style=tableStyle)
        flowable.append(table)

        p = Paragraph(text4, text4StyleCustom)
        flowable.append(p)

        p = Paragraph(getText5(group), text4StyleCustom)
        flowable.append(p)

        doc.build(flowable, onFirstPage=firstPageSetup)