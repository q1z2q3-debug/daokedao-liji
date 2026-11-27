# -*- coding: utf-8 -*-
"""v0.1.53 批（LJ304–LJ313）图二·义理图。"""
import os, sys
SK = os.environ.get("YILI_FIG_SKILL",
                    "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig")
sys.path.insert(0, os.path.join(SK, "scripts"))
from figkit import Fig, P, INK, OCH, BR, LINE, LG

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "assets", "fig")

# ---- 304 数从屋来 ----
f = Fig("池视重霤：数从屋来", "lj304b-chi-shi")
rows = [("天子", 4, 150), ("诸侯", 3, 200), ("大夫", 2, 250), ("士", 1, 300)]
for name, n, y in rows:
    f.t(96, y + 4, name, 11, INK, 'end')
    for i in range(n):
        f.line(150 + i * 18, y - 9, 150 + i * 18, y + 9, BR, 1.0)
    f.t(240, y + 4, "重霤", 9, LG)
    for i in range(n):
        f.line(330 + i * 18, y - 9, 330 + i * 18, y + 9, OCH if (n == 4) else BR, 1.0)
    f.t(420, y + 4, "池", 9, OCH if (n == 4) else LG)
    f.line(286, y, 322, y, LINE, 0.8, "3,3")
f.t(380, 348, "此数不问爵等表，只问其生时那间屋", 10, LG)
f.t(380, 372, "各视生时重霤", 11, INK)
f.concl("丧车象宫室：形似而用废，取其数与名")
f.save(OUT)

# ---- 305 备而示之未成 ----
f = Fig("备而示之未成", "lj305b-sui-yi-qi")
f.rect(232, 142, 300, 210, BR, P, 1.0)
f.rect(246, 156, 272, 182, LINE, P, 0.8)
for i, y in enumerate([190, 216, 242, 268]):
    f.line(250, y, 514, y, OCH if i == 0 else BR, 1.0 if i else 1.4)
f.t(536, 194, "岁一漆", 10, OCH, 'start')
f.t(536, 220, "岁一漆", 10, BR, 'start')
f.t(536, 246, "岁一漆", 10, BR, 'start')
f.t(536, 272, "岁一漆", 10, BR, 'start')
f.rect(300, 296, 70, 34, BR, LINE, 1.0)
f.t(335, 318, "藏", 11, INK)
f.t(560, 320, "虚之", 9, LG, 'start')
f.t(560, 336, "不令", 9, LG, 'start')
f.t(382, 392, "每年添一道，永远差一道——若未成然", 10, LG)
f.concl("备而示之未备，才不逼人")
f.save(OUT)

# ---- 306 六事并作 ----
f = Fig("六事并作，不依次第", "lj306b-bing-zuo")
f.rect(120, 112, 150, 46, BR, P, 1.0)
f.t(195, 140, "复", 12, INK)
f.rect(305, 112, 150, 46, BR, P, 1.0)
f.t(380, 140, "楔齿", 12, INK)
f.rect(490, 112, 150, 46, BR, P, 1.0)
f.t(565, 140, "缀足", 12, INK)
f.rect(120, 340, 150, 46, BR, P, 1.0)
f.t(195, 368, "饭", 12, INK)
f.rect(305, 340, 150, 46, BR, P, 1.0)
f.t(380, 368, "设饰", 12, INK)
f.rect(490, 340, 150, 46, BR, P, 1.0)
f.t(565, 368, "帷堂", 12, INK)
f.rect(300, 218, 160, 62, OCH, P, 1.2)
f.t(380, 244, "并作", 14, INK)
f.t(380, 266, "六事同在一帷下", 9, LG)
for x in (195, 380, 565):
    f.line(x, 160, 380 if x == 380 else x, 218, LINE, 1.0, "3,3")
    f.line(x, 340, 380 if x == 380 else x, 280, LINE, 1.0, "3,3")
f.line(195, 200, 380, 218, LINE, 0.8, "3,3")
f.line(565, 200, 380, 218, LINE, 0.8, "3,3")
f.line(195, 316, 380, 280, LINE, 0.8, "3,3")
f.line(565, 316, 380, 280, LINE, 0.8, "3,3")
f.concl("六事之下，是一具正在变硬变冷的身体")
f.save(OUT)

# ---- 307 代劳不代名 ----
f = Fig("可以代其劳，不可代其名", "lj307b-bu-dai-ming")
f.rect(110, 146, 170, 74, BR, P, 1.0)
f.t(195, 176, "父兄", 12, INK)
f.t(195, 200, "代命", 10, LG)
f.arr(284, 183, 456, 183, BR, 1.2)
f.rect(460, 146, 180, 74, BR, P, 1.0)
f.t(550, 176, "使者", 12, INK)
f.t(550, 200, "赴于有恩识者", 9, LG)
f.rect(300, 300, 170, 60, OCH, P, 1.2)
f.t(385, 336, "犹称孝子名", 12, INK)
f.line(385, 300, 385, 226, LINE, 1.0, "4,4")
f.t(398, 264, "名不代", 9, OCH, 'start')
f.t(380, 396, "代的是差遣之劳，不是丧主之位", 10, LG)
f.concl("丧主之名是丧事成立的根本，名一易，丧就不是他的丧")
f.save(OUT)

# ---- 308 求之愈备 ----
f = Fig("复于六处：求之愈备，愈知其不返", "lj308b-liu-chu")
f.line(120, 250, 646, 250, BR, 1.0)
spots = [(148, "小寝"), (248, "大寝"), (348, "小祖"), (438, "大祖"), (528, "库门"), (612, "四郊")]
for x, name in spots:
    f.dot(x, 250, 4, INK)
    f.t(x, 282, name, 10, INK)
f.line(612, 250, 660, 250, LINE, 1.0, "4,4")
f.ring(670, 250, 8, OCH, 1.2)
f.t(670, 288, "不返", 9, OCH)
f.t(380, 330, "六处皆其平生所至：寝、庙、门、郊", 10, LG)
f.t(380, 356, "招完一处，转向下一处——六次落空", 10, LG)
f.concl("这不是重复，是搜索：有对象的搜索是备，无对象的重复是赘")
f.save(OUT)

# ---- 309 巾与不巾 ----
f = Fig("盖不盖，看案上是什么", "lj309b-jin-yu-bu-jin")
for cx, covered, label in [(200, True, "有牲肉"), (520, False, "脯醢")]:
    f.path(f"M{cx-70},250 Q{cx},320 {cx+70},250 Z", BR, LINE, 1.0)
    if covered:
        f.line(cx - 78, 246, cx + 78, 246, OCH, 1.4)
        f.line(cx - 74, 246, cx - 74, 268, OCH, 1.0)
        f.line(cx + 74, 246, cx + 74, 268, OCH, 1.0)
    f.t(cx, 344, label, 11, INK)
f.t(200, 366, "则巾之", 9, LG)
f.t(520, 366, "则不巾", 9, LG)
f.t(380, 130, "同一脯醢，在室不巾，在堂则巾——为其在堂，恐埃尘", 10, LG)
f.concl("礼之大半，是先解决会不会脏，再说合不合敬")
f.save(OUT)

# ---- 310 豫 ----
f = Fig("殡后十日布材：木宜干腊", "lj310b-yu-cai")
f.line(110, 250, 470, 250, BR, 1.0)
f.dot(140, 250, 4, INK)
f.t(140, 232, "殡", 10, INK)
f.dot(300, 250, 4, INK)
f.t(300, 232, "旬", 10, INK)
f.arr(300, 250, 456, 250, OCH, 1.2)
f.dot(456, 250, 4, OCH)
f.t(456, 232, "布材", 10, OCH)
f.t(300, 282, "十日", 9, LG)
for i in range(4):
    f.line(520, 300 + i * 22, 700, 300 + i * 22, BR, 1.2)
f.t(610, 296, "椁材 · 明器之材", 9, LG)
f.t(610, 396, "堆而曝之，待其干", 9, LG)
f.t(300, 340, "期尚有余：三月而葬", 10, LG)
f.concl("不早则木不能用——礼的权威，一大半来自可验")
f.save(OUT)

# ---- 311 两刻守候 ----
f = Fig("朝奠日出，夕奠逮日", "lj311b-ri-chu-dai-ri")
f.line(380, 100, 380, 420, LINE, 0.8)
f.path("M120,190 Q190,130 260,190", OCH, P, 1.2)
f.t(190, 220, "日出", 10, INK)
f.rect(150, 268, 82, 40, BR, P, 1.0)
f.path("M166,268 Q191,292 216,268 Z", BR, LINE, 1.0)
f.t(191, 328, "朝奠", 9, LG)
f.path("M490,150 Q560,196 630,150", OCH, P, 1.2)
f.t(560, 220, "逮日", 10, INK)
f.rect(520, 268, 82, 40, BR, P, 1.0)
f.path("M536,268 Q561,292 586,268 Z", BR, LINE, 1.0)
f.t(561, 328, "夕奠", 9, LG)
f.t(380, 372, "两处都是昼夜交替之刻——界上", 10, LG)
f.concl("庶几遇之：不敢说他一定在，也不肯说他一定不在")
f.save(OUT)

# ---- 312 哭无时，反有祭 ----
f = Fig("哭无时，而反必有祭", "lj312b-ku-wu-shi")
rows = [(118, 430, "初丧", "哭不绝声"), (176, 330, "殡后", "庐中思忆则哭"), (234, 220, "小祥后", "哀至而哭")]
for y, w, tag, note in rows:
    f.rect(150, y, w, 34, BR, P, 1.0)
    f.t(160, y + 22, tag, 10, INK, 'start')
    f.t(150 + w - 12, y + 22, note, 9, LG, 'end')
f.line(120, 300, 690, 300, LINE, 0.8)
f.arr(300, 320, 460, 320, BR, 1.2)
f.t(380, 344, "君使之", 9, LG)
f.arr(460, 352, 300, 352, OCH, 1.4)
f.t(380, 376, "反必有祭：我回来了", 10, OCH)
f.t(380, 406, "出必告、反必面——对象换了，线没断", 10, LG)
f.concl("祭告不是给神的，是完成一件未完成的关系")
f.save(OUT)

# ---- 313 由凶向文·渐 ----
f = Fig("由凶向文：一处一处地回", "lj313b-jian-wen")
BASE = 372
items = [("练衣", 66, False), ("要绖", 96, False), ("绳屦", 126, False),
         ("角瑱", 156, False), ("鹿裘", 186, False), ("裼可", 216, True)]
for i, (name, h, och) in enumerate(items):
    x = 112 + i * 102
    f.rect(x, BASE - h, 84, h, OCH if och else BR, LINE, 1.4 if och else 1.0)
    f.t(x + 42, BASE + 22, name, 10, INK)
f.line(100, BASE, 720, BASE, BR, 1.0)
f.t(380, 130, "减（去首绖）· 加（练、縓缘、角瑱、广长、袪、裼）· 不变（无絇）", 9, LG)
f.concl("全恢复则丧不存在，不恢复则人活不下去")
f.save(OUT)

for name in []:
    pass
print("done")
