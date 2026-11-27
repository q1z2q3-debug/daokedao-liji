#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""取《礼记正义》（陕西师大十三经站）某一卷的注疏文本，剥净存 txt。

用法：
    python3 scripts/fetch_zhushu.py --juan 8
    python3 scripts/fetch_zhushu.py --juan 9 --out sources/卷九-檀弓下-2138.txt

页号随卷递减：卷三 2144、卷四 2143、卷五 2142、卷六 2141、卷七 2140、卷八 2139、卷九 2138。
存到 sources/ 里，不再依赖 /tmp（/tmp 会被清空）。

结构提醒：part K = 疏(K) + 经注(K+1)。即每块头是本节的疏，尾是下一节的经文＋郑注。
取某节材料要「疏取本块头、经注取本块尾」。底本简繁混用，勿用繁体 anchor 硬 rfind。
"""
import argparse
import html
import os
import re
import sys
import urllib.request

BASE = "http://ssjdd.snnu.edu.cn/sbw/info/1034/{n}.htm"

# 卷次 → 页号
PAGES = {3: 2144, 4: 2143, 5: 2142, 6: 2141, 7: 2140, 8: 2139, 9: 2138}
# 卷次 → 存档文件名
NAMES = {
    3: "卷三-曲礼上-2144.txt",
    4: "卷四-曲礼下-2143.txt",
    5: "卷五-曲礼下-2142.txt",
    6: "卷六-檀弓上-2141.txt",
    7: "卷七-檀弓上-2140.txt",
    8: "卷八-檀弓上-2139.txt",
    9: "卷九-檀弓下-2138.txt",
}


def strip_html(raw: str) -> str:
    raw = re.sub(r"<script.*?</script>", "", raw, flags=re.S)
    raw = re.sub(r"<style.*?</style>", "", raw, flags=re.S)
    raw = re.sub(r"<[^>]+>", "\n", raw)
    raw = html.unescape(raw).replace("\xa0", " ")
    lines = [l.strip() for l in raw.split("\n")]
    return "\n".join([l for l in lines if l])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--juan", type=int, required=True, help="卷次（3–9）")
    ap.add_argument("--out", default=None, help="输出路径，默认 sources/<卷名>.txt")
    ap.add_argument("--keep-html", action="store_true", help="同时保留原始 html 到 /tmp")
    a = ap.parse_args()

    n = PAGES.get(a.juan)
    if not n:
        sys.exit(f"未收录的卷次：{a.juan}（已收录 {sorted(PAGES)}）")
    url = BASE.format(n=n)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "ignore")

    txt = strip_html(raw)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = a.out or os.path.join(root, "sources", NAMES[a.juan])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(txt)
    if a.keep_html:
        with open(f"/tmp/{n}.htm", "w", encoding="utf-8") as fh:
            fh.write(raw)
    print(f"{out}  {len(txt.encode()):,} 字节  [疏]×{txt.count('[疏]')}")


if __name__ == "__main__":
    main()
