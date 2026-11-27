# -*- coding: utf-8 -*-
"""v0.1.39 图二：LJ192–LJ201（曲礼下 二·六十九 至 二·七十八）。"""
import os, sys
SKILL = os.environ.get("YILI_FIG_SKILL",
        "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts")
sys.path.insert(0, SKILL)
from figkit import Fig, P, INK, OCH, BR, LINE, LG
OUT = "/home/user/Doubao/chats/38456306325807874/daokedao-liji/assets/fig"

# ---------- 192 支子不祭 ----------
f = Fig("支子不祭，祭必告于宗子", "lj192b-zhi-zi")
# 庙
f.rect(310,118,150,78,BR,P,1.0)
f.parts.append(f'<path d="M296,118 L385,80 L474,118" fill="none" stroke="{BR}" stroke-width="1.3"/>')
f.t(385,168,"祖祢之庙",11,LG,'middle',1)
f.t(385,232,"宗子",11,INK,'middle',1)
f.rect(362,246,46,120,BR,P,1.0)
for x,lab in [(196,"支子"),(556,"支子")]:
    f.rect(x,272,42,94,BR,P,1.0)
    f.t(x+21,262,lab,11,INK,'middle',1)
# 左支子：告
f.line(217,270,332,120,BR,1.0)
f.rect(258,190,18,18,BR,P,1.2)
f.t(267,182,"告",10,OCH,'middle')
# 右支子：不祭（近庙处截断）
f.line(577,270,452,120,BR,1.0)
f.gap(505,182,518,172,4)
f.t(545,196,"不祭",10,BR,'middle')
# 案线
f.line(160,376,600,376,BR,1.0)
f.gap(556,376,592,376,4)
f.t(380,404,"庙在适子之家，支子无主祭之名",11,BR,'middle',1)
f.concl("庙在谁家，祭权就在谁手")
f.save(OUT)

# ---------- 193 号牲物 ----------
f = Fig("凡祭宗庙之礼：一物一号", "lj193b-hao-sheng")
rows = [(148,3,"牲八名"),(208,3,"鱼脯三名"),(268,2,"水酒二名"),(328,6,"谷蔬盐六名"),(388,2,"玉币二名")]
for y,n,note in rows:
    f.rect(150,y-13,36,26,BR,P,1.0)
    for i in range(n):
        f.dot(214+i*30,y,6,INK if y<380 else OCH)
    f.arr(190,y,204,y,BR,1.0)
    f.t(690,y+4,note,10,LG,'end')
f.t(168,120,"物",10,LG,'middle')
f.t(300,120,"号",10,LG,'middle')
f.t(380,424,"号者，所以别于人用",11,BR,'middle',1)
f.concl("同一个东西，人用与祭用不同名")
f.save(OUT)

# ---------- 194 崩薨卒不禄死 ----------
f = Fig("天子死曰崩，诸侯曰薨", "lj194b-beng-hong")
rows = [(132,470,13,"崩"),(170,404,11,"薨"),(208,338,9,"卒"),(246,272,7.5,"不禄"),(284,206,6,"死")]
for y,ln,r,lab in rows:
    f.line(150,y,150+ln,y,BR,1.0)
    f.ring(150+ln,y,r,BR,1.0)
    f.t(140,y+4,lab,11,INK,'end')
f.rect(200,344,120,62,BR,P,1.0)
f.line(230,375,290,375,BR,1.6)
f.t(260,336,"在床",10,INK,'middle',1)
f.rect(440,344,120,62,BR,P,1.0)
f.line(498,360,498,392,BR,1.6)
f.t(500,336,"在棺",10,INK,'middle',1)
f.arr(328,375,432,375,OCH,1.4)
f.t(380,398,"尸→柩",10,LG,'middle')
f.concl("名不是遮掩，是坚持贵贱之别")
f.save(OUT)

# ---------- 195 降渍 ----------
f = Fig("羽鸟曰降，四足曰渍", "lj195b-jiang-zi")
for i in range(3):
    f.line(250+i*52,142,288+i*52,196,BR,1.4)
f.line(180,200,580,200,BR,1.2)
f.t(380,226,"降：飞者落地",10,LG,'middle',1)
f.line(60,248,700,248,LINE,0.9)
f.line(300,320,460,320,BR,1.0)
f.parts.append(f'<circle cx="300" cy="320" r="22" fill="{OCH}" stroke="{BR}" stroke-width="1.0"/>')
f.ring(380,320,22,BR,1.0)
f.ring(460,320,22,BR,1.0)
f.parts.append(f'<ellipse cx="380" cy="320" rx="140" ry="42" fill="none" stroke="{BR}" stroke-width="1.0" stroke-dasharray="4,4"/>')
f.t(380,392,"渍：一死则余者相染",10,LG,'middle',1)
f.concl("飞者落地，群者相染")
f.save(OUT)

# ---------- 196 兵与皇 ----------
f = Fig("死寇曰兵，祭王父曰皇祖考", "lj196b-bing-huang")
f.rect(348,112,54,74,BR,P,1.0)
f.line(330,104,424,190,OCH,2.4)
f.t(300,120,"兵",11,INK,'end')
f.rect(356,214,40,52,BR,P,1.0)
f.arr(376,190,376,210,BR,1.0)
f.t(414,244,"飨禄其后",10,LG,'start')
f.line(60,282,700,282,LINE,0.9)
pairs = [(170,"旧称"),(370,"旧称"),(560,"旧称")]
for x,_ in pairs:
    f.rect(x,320,34,44,BR,P,1.0)
    f.rect(x+46,312,34,58,BR,P,1.0)
    f.line(x+34,340,x+46,340,BR,1.0)
f.t(280,410,"旧称改尊号，加皇于祭",11,BR,'middle',1)
f.concl("一以死法定名，一以祭位定名")
f.save(OUT)

# ---------- 197 生死异称 ----------
f = Fig("生曰父、母、妻，死曰考、妣、嫔", "lj197b-sheng-si")
f.t(258,132,"生称",11,INK,'middle',2)
f.t(498,132,"死称",11,INK,'middle',2)
rows = [(150,58),(240,58),(330,58)]
for y,h in rows:
    f.rect(230,y,56,h,BR,P,1.0)
    f.rect(470,y,56,h+6,BR,P,1.0)
    f.line(288,y+29,470,y+29,BR,0.9)
    f.gap(370,y+29,384,y+29,3)
f.dot(546,374,4,OCH)
f.t(556,378,"有法度",10,OCH,'start')
f.t(380,428,"三对六名，同一人不可共一称",10,BR,'middle')
f.concl("一字的距离，就是生死的距离")
f.save(OUT)

# ---------- 198 寿考短折 ----------
f = Fig("寿考曰卒，短折曰不禄", "lj198b-shou-kao")
f.line(130,170,620,170,BR,1.0)
f.dot(130,170,4,BR)
f.rect(620,130,58,80,BR,P,1.0)
f.t(600,168,"寿考",11,INK,'end')
f.line(130,300,412,300,BR,1.0)
f.line(400,300,412,318,BR,1.2)
f.dot(130,300,4,BR)
f.rect(620,285,58,56,BR,P,1.0)
f.t(600,296,"短折",11,INK,'end')
f.line(649,212,649,283,BR,1.0,"3,3")
f.gap(649,240,649,256,5)
f.t(638,252,"卒／不禄",10,LG,'end')
f.t(380,392,"德同而年异，所借之名亦异",11,BR,'middle',1)
f.concl("德同而年异，名亦异")
f.save(OUT)

# ---------- 199 视之界 ----------
f = Fig("视之界：袷与带", "lj199b-shi-jie")
f.rect(420,110,70,270,BR,P,1.0)
f.line(420,190,490,190,OCH,1.2)
f.line(420,290,490,290,OCH,1.2)
f.t(504,194,"袷",10,INK,'start')
f.t(504,294,"带",10,INK,'start')
f.line(150,160,404,176,BR,1.0)
f.xmark(406,178,6,BR,1.0)
f.t(268,146,"上于袷则敖",10,LG,'middle')
f.line(150,240,404,240,BR,1.2)
f.t(268,228,"袷带之间，合法之视",10,INK,'middle')
f.line(150,322,404,306,BR,1.0)
f.xmark(406,304,6,BR,1.0)
f.t(172,344,"下于带则忧",10,LG,'start')
f.parts.append(f'<path d="M140,286 Q300,362 410,348" fill="none" stroke="{OCH}" stroke-width="1.2" stroke-dasharray="5,3"/>')
f.xmark(410,348,6,OCH,1.3)
f.t(124,292,"倾",10,OCH,'middle')
f.t(380,408,"袷与带，是臣视天子的两界",11,BR,'middle',1)
f.concl("越尊，别人看他的余地越小")
f.save(OUT)

# ---------- 200 言之所 ----------
f = Fig("君命，在官言官", "lj200b-yan-zhi-suo")
f.line(90,160,660,160,BR,1.1)
f.t(375,148,"君命",11,INK,'middle',2)
boxes = [90,240,390,540]
labs = ["官","府","库","朝"]
for x,lab in zip(boxes,labs):
    f.line(x+60,160,x+60,224,BR,1.0)
    f.rect(x,224,120,100,BR,P,1.0)
    f.t(x+12,248,lab,11,INK,'start')
for i in range(3):
    f.line(148,272+i*18,222,272+i*18,BR,1.0)
f.ring(300,290,13,BR,1.2)
f.ring(432,288,10,BR,1.2); f.ring(466,288,10,BR,1.2); f.line(432,306,466,306,BR,1.0)
f.line(578,258,578,300,BR,1.4); f.line(602,258,602,300,BR,1.4)
# 辍朝而顾：自朝位回望
f.parts.append(f'<path d="M600,336 Q500,392 404,362" fill="none" stroke="{BR}" stroke-width="1.0"/>')
f.xmark(404,360,6,OCH,1.3)
f.t(506,404,"辍朝而顾谓之固",10,OCH,'middle',1)
f.t(300,336,"朝言不及犬马",10,BR,'middle',1)
f.concl("在什么地方，说什么话")
f.save(OUT)

# ---------- 201 大飨 ----------
f = Fig("大飨不问卜，不饶富", "lj201b-bu-wen-bu")
f.parts.append(f'<ellipse cx="360" cy="170" rx="96" ry="46" fill="{P}" stroke="{BR}" stroke-width="1.2"/>')
for dx,dy in [(0,0),(24,8),(-26,10)]:
    f.line(330+dx,150+dy,350+dx,168+dy,BR,1.2)
    f.line(350+dx,168+dy,362+dx,162+dy,BR,1.2)
f.line(508,132,508,200,BR,1.2)
f.xmark(508,204,7,OCH,1.4)
f.t(524,196,"不问卜",10,LG,'start')
f.line(60,250,700,250,LINE,0.9)
f.rect(250,300,100,70,BR,P,1.0)
f.line(250,300,350,300,BR,1.4)
f.rect(450,300,100,70,BR,P,1.0)
f.rect(450,272,100,28,OCH,P,1.0)
f.line(450,300,550,300,OCH,1.4)
f.xmark(500,272,8,OCH,1.4)
f.t(350,392,"备而已",10,LG,'middle',1)
f.t(500,392,"多于礼",10,OCH,'middle',1)
f.concl("礼所谓富，不是多，是全")
f.save(OUT)
print("LJ192–LJ201 十图已生成")
