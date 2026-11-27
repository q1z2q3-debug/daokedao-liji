# -*- coding: utf-8 -*-
"""v0.1.40 图二：LJ202–LJ203（曲礼下 二·七十九、二·八十，收篇）。"""
import os, sys
SKILL = os.environ.get("YILI_FIG_SKILL",
        "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts")
sys.path.insert(0, SKILL)
from figkit import Fig, P, INK, OCH, BR, LINE, LG
OUT = "/home/user/Doubao/chats/38456306325807874/daokedao-liji/assets/fig"

# ---------- 202 凡挚 ----------
f = Fig("凡挚：六等之物，一义「至」", "lj202b-zhi-zhi")
f.ring(380,168,15,OCH,1.6)
f.t(380,150,"至",11,OCH,'middle')
rows = [(120,"天子鬯"),(224,"诸侯圭"),(320,"卿羔"),(420,"大夫雁"),(520,"士雉"),(614,"庶人鹜")]
for x,lab in rows:
    f.line(x,336,380,182,BR,0.9)
    f.rect(x-13,336,26,20,BR,P,1.0)
    f.t(x,378,lab,10,LG,'middle')
f.line(96,358,636,358,LINE,0.9)
f.line(60,398,700,398,LINE,0.9)
f.t(380,424,"所执不同，所表者同：我已到此",11,BR,'middle',1)
f.concl("挚不是一个东西，是一句「到了」")
f.save(OUT)

# ---------- 203 纳女 ----------
f = Fig("纳女：一辞三降", "lj203b-nei-nv")
steps = [(140,160,300,"于天子曰「备百姓」",INK),
         (300,230,460,"于国君曰「备酒浆」",INK),
         (460,300,620,"于大夫曰「备埽洒」",OCH)]
for x1,y,x2,lab,col in steps:
    f.line(x1,y,x2,y,BR,1.4)
    f.line(x2,y,x2,y+70,BR,1.0)
    f.rect(x1+18,y-20,26,18,BR,P,1.0)
    f.t(x1+56,y-7,lab,10,col,'start')
f.line(110,150,110,300,BR,1.0)
f.arr(110,300,110,318,BR,1.1)
f.t(110,140,"位",10,LG,'middle')
f.line(60,410,700,410,LINE,0.9)
f.t(600,388,"不及士",10,LG,'end')
f.t(380,412,"辞愈卑，位愈下",11,BR,'middle',1)
f.concl("一句谦辞，量的是位置")
f.save(OUT)
print("LJ202–LJ203 二图已生成")
