# -*- coding: utf-8 -*-
import os, sys
SK = os.environ.get("YILI_FIG_SKILL", "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig")
sys.path.insert(0, os.path.join(SK, "scripts"))
from figkit import Fig, P, INK, OCH, BR, LINE, LG

OUT = "/home/user/Doubao/chats/38456306325807874/daokedao-liji/assets/fig"


def man(fig, x, base, h=52, head=7, color=BR):
    fig.ring(x, base - h, head, INK, 1.2)
    fig.line(x, base - h + head, x, base, color, 1.1)
    fig.line(x - 9, base - h + 18, x + 9, base - h + 18, LG, 0.9)


# ---------- 413 守胜知 ----------
f = Fig("受教者失礼，鲁钝者守礼", "lj413b-shi-li-sheng-xue")
f.line(90, 400, 670, 400, BR, 1.2)
man(f, 200, 400, 62)
f.rect(206, 350, 30, 16, BR, P, 1.0)
f.line(206, 358, 236, 358, LG, 0.8)
f.line(214, 350, 214, 366, LG, 0.8)
f.path("M164,400 L172,360 L226,360 L234,400", BR, P, 1.1)
f.gap(184, 386, 196, 380, 5)
f.t(200, 424, "受教而失", 9, LG)
man(f, 470, 400, 54)
f.path("M446,400 L446,364 L494,364 L494,400", BR, P, 1.0)
f.line(444, 372, 470, 372, BR, 0.9)
f.line(446, 382, 494, 382, LG, 0.9)
f.line(458, 342, 470, 348, BR, 1.0)
f.line(482, 342, 470, 348, BR, 1.0)
f.t(470, 424, "鲁钝而守", 9, LG)
f.ring(600, 300, 16, OCH, 1.2)
f.line(600, 290, 600, 310, OCH, 0.8)
f.t(600, 336, "无禁", 9, OCH)
f.concl("虽鲁钝，其於礼胜学")

f.save(OUT)

# ---------- 414 三物错位 ----------
f = Fig("三物错位：服不为兄", "lj414b-xie-kuang-chan-rui")
# 行一 蚕 / 蟹
f.path("M146,176 Q160,160 176,172 Q190,184 206,168", BR, P, 1.1)
for q in (158, 172, 186):
    f.line(q, 168, q, 178, LG, 0.8)
f.path("M300,182 L300,156 L348,156 L348,182 Z", BR, P, 1.1)
f.line(300, 156, 300, 148, BR, 0.9)
f.line(348, 156, 348, 148, BR, 0.9)
f.arr(352, 170, 216, 170, BR, 1.1)
# 行二 蜂 / 蝉
f.ring(170, 262, 10, BR, 1.0)
f.line(156, 254, 184, 254, BR, 1.2)
f.ring(322, 262, 10, BR, 1.0)
f.line(322, 272, 322, 292, BR, 1.2)
f.line(316, 288, 328, 288, BR, 0.9)
f.arr(336, 262, 200, 262, BR, 1.1)
# 行三 兄 / 子皋
f.ring(168, 350, 9, BR, 1.0)
f.line(168, 359, 168, 384, BR, 1.1)
f.path("M152,384 L152,372 L184,372 L184,384", BR, P, 1.0)
f.rect(312, 344, 30, 24, BR, P, 1.0)
f.line(312, 356, 342, 356, LG, 0.8)
f.arr(342, 366, 196, 366, BR, 1.1)
f.t(250, 196, "匡在蟹", 8, LG)
f.t(250, 288, "緌在蝉", 8, LG)
f.t(250, 392, "衰在子皋", 8, LG)
f.line(120, 400, 640, 400, LINE, 0.9, "4,3")
f.concl("服是子皋为之，非为兄施")

f.save(OUT)

# ---------- 415 五日不食 ----------
f = Fig("五日不食：情在虚处", "lj415b-wu-ri-bu-shi")
for i, x in enumerate((240, 300, 360)):
    f.line(x, 200, x, 250, BR, 1.2)
f.line(220, 250, 380, 250, BR, 0.9)
for i, x in enumerate((420, 470)):
    f.line(x, 200, x, 250, OCH, 1.0, "5,4")
f.line(404, 250, 486, 250, OCH, 0.9)
f.path("M228,150 Q300,120 372,150", BR, 'none', 1.2)
f.gap(352, 143, 386, 155, 6)
f.line(90, 330, 500, 330, BR, 1.2)
man(f, 240, 330, 46)
f.line(228, 300, 216, 330, BR, 1.0)
f.line(252, 300, 264, 330, BR, 1.0)
f.rect(540, 168, 90, 56, BR, P, 0.9, "4,3")
f.line(540, 196, 500, 250, LG, 0.9, "3,3")
f.t(212, 302, "三日为节", 8, LG, 'end')
f.t(470, 292, "过二日", 8, OCH)
f.concl("自吾母而不得吾情，吾恶乎用吾情")

f.save(OUT)

# ---------- 416 三问三答 ----------
f = Fig("三问三答：两不可，一可", "lj416b-san-wen-san-da")
for i, x in enumerate((140, 320, 500)):
    f.rect(x, 150, 130, 96, BR, P, 1.0)
# 框一 仰面人 + 日
f.ring(196, 190, 8, INK, 1.0)
f.line(196, 198, 196, 226, BR, 1.1)
f.line(208, 178, 216, 166, LG, 0.9)
f.ring(226, 210, 7, BR, 0.9)
f.xmark(228, 174, 16, OCH, 1.8)
# 框二 巫
f.ring(386, 190, 8, INK, 1.0)
f.line(386, 198, 386, 226, BR, 1.1)
f.line(378, 176, 394, 176, BR, 1.0)
f.ring(416, 210, 7, BR, 0.9)
f.xmark(418, 174, 16, OCH, 1.8)
# 框三 市
for r in range(2):
    for c in range(3):
        f.rect(534 + c * 30, 186 + r * 26, 22, 18, BR, P, 0.9)
# 下排 巷市
f.line(140, 320, 630, 320, BR, 1.2)
for c in range(8):
    f.rect(160 + c * 58, 320, 44, 22, BR, P, 0.9)
f.line(140, 388, 630, 388, LINE, 0.9, "4,3")
f.concl("忧戚於旱，若居丧者")

f.save(OUT)

# ---------- 417 一离一合 ----------
f = Fig("一离一合，孔子取合", "lj417b-li-yu-he")
f.rect(96, 190, 220, 120, BR, P, 1.2)
f.rect(120, 214, 76, 72, BR, P, 1.0)
f.rect(216, 214, 76, 72, BR, P, 1.0)
f.line(196, 210, 196, 292, BR, 1.0)
f.t(206, 336, "卫：离之", 9, LG)
f.rect(400, 190, 220, 120, BR, P, 1.2)
f.rect(424, 214, 76, 72, BR, P, 1.0)
f.rect(500, 214, 76, 72, BR, P, 1.0)
f.line(500, 214, 500, 286, OCH, 1.8)
f.t(510, 336, "鲁：合之", 9, LG)
man(f, 680, 310, 52)
f.line(666, 262, 640, 250, BR, 1.0)
f.line(694, 262, 720, 250, BR, 1.0)
f.t(680, 336, "善夫", 9, OCH)
f.concl("穀则异室，死则同穴")

f.save(OUT)
print("done")
