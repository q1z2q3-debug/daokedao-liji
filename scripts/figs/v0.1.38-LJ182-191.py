# -*- coding: utf-8 -*-
"""v0.1.38 图二生成脚本：礼记 曲礼下 二·五十九 至 二·六十八（LJ182–LJ191）。

工具（Fig 画具）在技能 runze-daokedao-yili-fig/scripts/figkit.py，不随本仓分发。
    python3 scripts/figs/v0.1.38-LJ182-191.py
产物写 assets/fig/<key>.svg。目检：
    python3 $SKILL/scripts/render_check.py --dir assets/fig --keys <逗号分隔十键> --out /tmp/batch.png
"""
import os, sys
SKILL = os.environ.get("YILI_FIG_SKILL",
        "/home/user/.doubao/agent_mode/workspace/.user_skills/runze-daokedao-yili-fig/scripts")
sys.path.insert(0, SKILL)
from figkit import Fig, P, INK, OCH, BR, LINE, LG
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "assets", "fig")

f=Fig("天子不言出，诸侯不生名","lj182b-bu-yan-chu")
f.rect(60,110,640,300,BR,P,1.0)
# 上带：天子
f.t(110,168,"天子",12,INK,'middle')
f.line(160,176,430,176,BR,1.0)          # 常笔
f.line(430,176,470,176,OCH,3.0)         # 断后之赭笔
f.t(495,172,"策书称君，不言出",11,LG,'start')
f.t(300,196,"出",11,OCH,'middle')
# 下带：诸侯
f.t(110,258,"诸侯",12,INK,'middle')
f.line(160,266,430,266,BR,1.0)
f.line(430,266,470,266,OCH,3.0)
f.t(495,262,"相见称爵，不生名",11,LG,'start')
f.t(300,286,"名",11,OCH,'middle')
f.line(80,320,680,320,LINE,0.8)
f.t(110,362,"君子",12,INK,'middle')
f.t(650,362,"恶",12,INK,'middle')
f.ring(150,352,14,BR,1.0)
f.ring(610,352,14,BR,1.0)
f.line(180,352,560,352,BR,0.9,"3,4")
f.parts.append(f'<line x1="356" y1="352" x2="384" y2="352" stroke="{P}" stroke-width="4"/>')
f.xmark(370,352,6,BR,1.0)
f.t(370,392,"不亲",11,BR,'middle')
f.t(370,412,"书出、书名，是刑不是笔",11,LG,'middle')
f.t(380,52,"天子不言出，诸侯不生名",15,INK,'middle',3)
f.concl("例外不是另外一种写法，是另外一种刑罚")
f.save(OUT)

f=Fig("不显谏：五等与一去","lj183b-bu-xian-jian")
ys=[130,175,220,265,310]
names=["讽","顺","直","争","赣"]
lws=[0.8,1.3,1.9,2.6,3.4]
rs=[11,9,7.5,6,4.5]
for i in range(5):
    y=ys[i]
    f.t(122,y+4,names[i],13,INK,'middle')
    f.line(150,y,600,y,INK,lws[i])
    f.ring(622,y,rs[i],BR if i<4 else OCH,1.0)
f.xmark(622,310,5,OCH,1.2)
f.t(622,340,"赣为下",10,LG,'middle')
f.t(375,340,"讽为上",10,LG,'middle')
f.line(60,352,700,352,LINE,0.8)
f.t(380,378,"线粗者谏激，圆小者礼轻",11,BR,'middle',1)
f.arr(300,404,700,404,OCH,1.4)
f.t(240,408,"三谏不听",11,INK,'middle')
f.t(712,408,"逃",11,OCH,'start')
f.concl("越激烈的谏，礼越看轻")
f.save(OUT)

f=Fig("同一个数字，两种收场","lj184b-hao-qi")
f.rect(60,110,300,300,BR,P,1.0)
f.t(210,142,"臣",12,INK,'middle',2)
f.rect(196,170,48,190,BR,P,1.0)
for i in range(3):
    h=34-i*8
    f.line(160+i*14,360,160+i*14,360-h,BR,1.0)
f.t(174,392,"三谏",10,LG,'middle')
f.arr(252,286,352,286,OCH,1.5)
f.t(300,330,"逃之",11,OCH,'middle')
f.rect(400,110,300,300,BR,P,1.0)
f.t(550,142,"子",12,INK,'middle',2)
f.rect(492,196,48,164,BR,P,1.0)
f.rect(556,196,48,164,BR,P,1.0)
for i in range(3):
    h=34-i*8
    f.line(456+i*14,360,456+i*14,360-h,BR,1.0)
f.t(470,392,"三谏",10,LG,'middle')
f.t(530,392,"随之",11,OCH,'middle')
f.line(380,120,380,400,LINE,0.9,"3,3")
f.t(380,52,"同一个数字，两种收场",15,INK,'middle',3)
f.concl("至亲无去：臣能走，子无处可走")
f.save(OUT)

f=Fig("尝是试受，不是试毒","lj185b-chang-yao")
def bowl(cx,cy,r,color=BR,lw=1.2):
    f.parts.append(f'<path d="M{cx-r},{cy} A{r},{r} 0 0 0 {cx+r},{cy}" fill="none" stroke="{color}" stroke-width="{lw}"/>')
    f.line(cx-r,cy,cx+r,cy,color,lw)
bowl(288,236,76,BR,1.3)
f.t(288,264,"君亲之疾",11,INK,'middle',1)
bowl(516,282,44,BR,1.3)
f.t(516,300,"臣子先尝",11,INK,'middle',1)
f.parts.append(f'<path d="M486,246 Q446,206 396,196" fill="none" stroke="{OCH}" stroke-width="1.4" marker-end="url(#ah)"/>')
f.t(430,178,"先尝而后进",10,OCH,'middle')
# 三代
for i,h in enumerate([34,27,20]):
    f.line(500+i*36,150,500+i*36,150+h,BR,1.2)
f.t(636,150,"三世相承",10,LG,'middle')
f.t(536,404,"医不三世，不服其药",11,BR,'middle',1)
f.line(60,340,380,340,LINE,0.8)
f.t(220,372,"尝者，度其所堪",11,INK,'middle',1)
f.concl("尝是先替人受一口，不是先替人试一毒")
f.save(OUT)

f=Fig("儗人必于其伦","lj186b-lun")
for i in range(3):
    f.rect(150+i*68,236,60,70,BR,P,1.0)
f.line(140,318,388,318,BR,1.0)
f.line(140,318,140,250,BR,1.0)
f.line(140,250,150,250,BR,1.0)
f.line(388,318,388,250,BR,1.0)
f.line(388,250,378,250,BR,1.0)
f.t(264,362,"同类相并",11,LG,'middle',1)
f.rect(492,236,60,70,BR,P,1.0)
f.rect(556,196,60,110,BR,P,1.0)
f.rect(620,236,60,70,BR,P,1.0)
f.t(556,330,"以贵比贱",11,OCH,'middle',1)
f.line(470,300,552,300,OCH,1.2,dash="3,3")
f.xmark(540,300,6,OCH,1.2)
f.line(60,392,700,392,LINE,0.8)
f.t(380,420,"比大夫当于大夫，比士当于士",11,BR,'middle',1)
f.concl("放错排不是抬高，是两伤")
f.save(OUT)

f=Fig("问年：答的是位置，不是年岁","lj187b-wen-nian")
xs=[132,252,372,492,612]
hs=[150,134,118,102,86]
labs=["天子","国君","大夫之子","士之子","庶人之子"]
for i in range(5):
    x=xs[i]; h=hs[i]; y=310-h
    f.rect(x-31,y,62,h,BR,P,1.0)
    f.t(x,y-10,labs[i],10,INK,'middle')
# 物
# 1 衣襟
f.line(112,346,152,346,BR,1.0); f.line(112,360,152,360,BR,1.0); f.line(132,338,132,368,OCH,1.6)
# 2 鼎
f.rect(236,344,32,20,BR,P,1.0)
f.line(238,364,238,372,BR,1.0); f.line(266,364,266,372,BR,1.0)
f.line(232,340,272,340,BR,1.0)
# 3 主事
f.line(372,368,372,342,BR,1.4); f.line(358,348,386,348,BR,1.2)
# 4 门
f.line(480,368,480,340,BR,1.2); f.line(504,368,504,340,BR,1.2); f.line(476,338,508,338,BR,1.2)
# 5 柴
for i in range(3):
    f.line(596+i*8,368,600+i*8,340,BR,1.0)
f.t(380,398,"五种问，五种答，无一处言年",11,BR,'middle',1)
f.concl("长幼不靠数字，靠本事；天子连本事也不许说")
f.save(OUT)

f=Fig("四等人，四种可算的富","lj188b-wen-fu")
gs=[(70,"国君"),(240,"大夫"),(410,"士"),(580,"庶人")]
for x,lab in gs:
    f.rect(x,150,140,220,BR,P,1.0)
    f.t(x+70,138,lab,11,INK,'middle',1)
# 1 地片
f.rect(108,236,64,64,BR,P,1.0)
for dx,dy in [(-6,-6),(70,-6),(-6,70),(70,70)]:
    f.line(108+dx,236+dy,108+dx+10*sign,236+dy,BR,1.0) if False else None
f.line(102,230,110,230,BR,1.0); f.line(102,230,102,238,BR,1.0)
f.line(170,230,178,230,BR,1.0); f.line(178,230,178,238,BR,1.0)
f.line(102,306,110,306,BR,1.0); f.line(102,306,102,298,BR,1.0)
f.line(170,306,178,306,BR,1.0); f.line(178,306,178,298,BR,1.0)
f.t(140,330,"数地",10,LG,'middle')
# 2 邑
f.rect(272,232,76,60,BR,P,1.0)
f.rect(304,262,18,30,OCH,P,1.2)
f.line(266,226,354,226,BR,1.2)
f.t(310,330,"有宰",10,LG,'middle')
# 3 车
f.ring(444,296,16,BR,1.2); f.ring(486,296,16,BR,1.2)
f.line(430,272,500,272,BR,1.2); f.line(444,272,444,296,BR,1.0); f.line(486,272,486,296,BR,1.0)
f.t(465,330,"车数",10,LG,'middle')
# 4 畜
for i in range(3):
    cx=614+i*24
    f.parts.append(f'<path d="M{cx-10},300 Q{cx},282 {cx+10},300" fill="none" stroke="{BR}" stroke-width="1.1"/>')
    f.line(cx-6,300,cx-6,310,BR,1.0); f.line(cx+6,300,cx+6,310,BR,1.0)
f.t(650,330,"畜数",10,LG,'middle')
f.t(380,392,"问的不是金帛，是最所优饶者",11,BR,'middle',1)
f.concl("不问有多少钱，问你有什么可算")
f.save(OUT)

f=Fig("祭之四等：逐级递减","lj189b-ji-deng")
f.rect(100,100,560,240,BR,P,1.0)
f.rect(170,132,420,184,BR,P,1.0)
f.rect(240,164,280,136,BR,P,1.0)
f.rect(310,196,140,76,BR,P,1.0)
f.t(112,118,"天子",10,INK,'start')
f.t(182,150,"诸侯",10,INK,'start')
f.t(252,182,"大夫",10,INK,'start')
f.t(322,214,"士",10,INK,'start')
for x in [200,320,440,560]:
    f.dot(x,332,4.5,OCH)
for x in [260,380,500]:
    f.dot(x,308,4.2,BR)
f.dot(380,292,4.2,BR)
f.dot(380,264,4.2,BR)
f.t(380,364,"天子：天地·四方·山川·五祀",11,INK,'middle',1)
f.t(380,390,"诸侯：方祀·山川·五祀　　大夫：五祀　　士：其先",10,BR,'middle',0)
f.concl("每一级减掉的，都是最上面那一项")
f.save(OUT)

f=Fig("凡祭：废与举","lj190b-fei-ju")
f.rect(60,110,300,240,BR,P,1.0)
f.rect(130,200,90,26,BR,P,1.0)
f.rect(236,200,64,26,BR,P,1.0)
f.line(200,190,200,146,BR,1.0,"3,3")
f.line(170,142,230,142,OCH,1.6)
f.t(210,124,"废之",10,INK,'middle')
f.t(210,270,"莫敢举",11,LG,'middle',1)
f.rect(400,110,300,240,BR,P,1.0)
f.rect(516,152,44,150,BR,P,1.0)
f.line(538,306,538,338,BR,1.0,"3,3")
f.line(512,342,564,342,OCH,1.6)
f.t(538,132,"举之",10,INK,'middle')
f.t(600,240,"莫敢废",11,LG,'middle',1)
f.rect(330,368,44,30,BR,P,1.0)
f.parts.append(f'<ellipse cx="352" cy="382" rx="64" ry="27" fill="none" stroke="{OCH}" stroke-width="1.1" stroke-dasharray="4,4"/>')
f.t(352,424,"非其所祭而祭　淫祀无福",10,OCH,'middle')
f.concl("礼守的不是祭，是废立之间那段空白")
f.save(OUT)

f=Fig("四等之牲：等级即时间的等级","lj191b-xi-sheng")
rows=[(152,"天子·牺牛","纯毛，涤三月",450),
      (222,"诸侯·肥牛","养于涤三月",390),
      (292,"大夫·索牛","求得即用",30),
      (362,"士·羊豕","羊豕，不过十日",40)]
f.line(210,124,210,392,BR,1.0)
for y,lab,note,ln in rows:
    f.rect(210,y-10,ln,20,BR,P,1.0)
    f.line(210,y-10,210,y+10,OCH,1.6)
    f.t(196,y-2,lab,11,INK,'end')
    f.t(196,y+13,note,9,LG,'end')
f.line(236,134,636,134,OCH,1.2)
f.t(644,132,"纯毛之择",9,OCH,'start')
f.t(380,398,"上得兼下，下不得僣上",11,BR,'middle',1)
f.t(380,418,"长者为备久，短者为备促",9,LG,'middle',1)
f.concl("规格的差别，常常就是准备时间的差别")
f.save(OUT)
print("LJ182–LJ191 十图已生成")
